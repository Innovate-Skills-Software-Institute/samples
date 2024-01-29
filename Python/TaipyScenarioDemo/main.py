from taipy import Config, Gui, Core
import taipy

def build_message(name: str):
    return f"Hello {name}!"


input_name = "Taipy"
message = None

def submit_scenario(state):
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()

page = """
Name: <|{input_name}|input|>
<|submit|button|on_action=submit_scenario|>
Message: <|{message}|text|>
"""

if __name__ == "__main__":
    Config.load("taipy_config.toml")
    Core().run()
    scenario_cfg = Config.scenarios["my_scenario"]
    scenario = taipy.create_scenario(scenario_cfg)
    Gui(page).run()