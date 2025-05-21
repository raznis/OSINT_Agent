from typing import Tuple, Any
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import TaskOutput
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import BraveSearchTool

from crewai.memory import LongTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

NO_INFORMATION_FOUND="no information found"

def validate_researcher_content(result: TaskOutput) -> Tuple[bool, Any]:
    """Validate research content meets requirements."""
    try:
        # print("In validate_researcher_content...")
        # Check word count
        word_count = len(result.raw.split())
        # print("Word Count:", word_count)
        # print(result.raw)

        if word_count < 100:
            return (False, "Not enough content")

        if NO_INFORMATION_FOUND in result.raw.lower():
            return (False, "Model says that no information was found")

        return (True, result)
    except Exception as e:
        print("The exception was:", e)
        return (False, "Unexpected error during validation")

@CrewBase
class Investigators():
    """Investigators crew"""

    #Agents
    agents_config = 'config/agents.yaml'
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool(save_file=True)],
            retry_on_fail=True,  # Enable retry
            max_retries=3,  # Set maximum retries
        )

    @agent
    def fincrime_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['fincrime_analyst'],
            verbose=False,
        )
    
    @agent
    def osint_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['osint_reporter'],
            verbose=False,
        )

    # Tasks
    tasks_config = 'config/tasks.yaml'

    

    @task
    def research_target(self) -> Task:
        
        
        return Task(
            config=self.tasks_config['research_target'],
            guardrail=validate_researcher_content,
        )

    @task
    def analyze_target(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_target'], 
        )
    
    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], 
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Investigators crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,
            # Long-term memory for persistent storage across sessions
            long_term_memory = LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path="./memory/long_term_memory_storage.db"
                )
            ),
           # Entity memory for tracking key information about entities
            entity_memory = EntityMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {
                            "model": 'text-embedding-3-small'
                        }
                    },
                    type="short_term",
                    path="./memory/"
                )
            ),
        )
