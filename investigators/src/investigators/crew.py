from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool



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
            tools=[SerperDevTool()],
            retry_on_fail=True,  # Enable retry
            max_retries=3  # Set maximum retries
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
        )
