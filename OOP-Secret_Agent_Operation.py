class Agent:
    total_agents = 0
    def __init__(self, code_name:str, clearance_level):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1
   
    def set_clearance_level(self, clearance_level):
        if clearance_level > 0 and clearance_level < 10:
            self._clearance_level = clearance_level
        else:
            print ("'Clearance level' must be greater than 0 and less than 10")

    def get_clearance_level(self):
        return self._clearance_level

    def report(self):
        return f'Agent: {self.code_name}. Clearance Level: {self._clearance_level}'

class Mission:
    def __init__(self, mission_name:str, target_location:str, assigned_agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        return f'Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}'
    
class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        return super().report() + f'. region: {self.region}'



a = FieldAgent('Avi', 2, 'Tel-Aviv')
b = FieldAgent('Eli', 8, 'Jerusalem')
c = FieldAgent('Itzik', -1, 'Bnei-Brak')
d = Agent('Moshe', 9)


agents:Agent = [a, b, c, d]
for agent in agents:
    agent.set_clearance_level(agent._clearance_level)
    print (agent.report())



@staticmethod
def get_total_agents(cls):
    return cls.total_agents

print (get_total_agents(Agent))


