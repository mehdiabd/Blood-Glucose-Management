import time

class TimelyStateMachine:

    def __init__(self, initial_state):
        self.state = initial_state
        self.transitions = {}

    def add_transition(self, event, next_state):
        self.transitions[event] = next_state

    def process_event(self, event):
        next_state = self.transitions.get(event)
        if next_state is not None:
            self.state = next_state

    def run(self):
        while True:
            time.sleep(5)
            event = input("Enter event: ")
            self.process_event(event)


if __name__ == "__main__":
    state_machine = TimelyStateMachine("sensing")
    state_machine.add_transition("idle", "Tx/Rx")
    state_machine.add_transition("Tx/Rx", "sensing")
    state_machine.run()