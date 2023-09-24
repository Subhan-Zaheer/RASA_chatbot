# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
import rasa_sdk
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
#
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

#     def name(self) -> Text:
#         return "action_fallback"

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="my_custom_fallback_template")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]

class ActionYes(Action):
    def name(self) -> Text:
        return "action_continue"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Implement logic to continue the conversation
        dispatcher.utter_message("Agr aapko lagta hai k aap ka opponent minor (child) ki tarbiyat, ya growth sahi nahi kr raha, ya us ne doosri shadi kr li hai, ya us k financial halaat ese nahi hain k wo achi growth kr ske, ya uska character sahi nahi hai to aap court me appeal kr skte hain guardianship ka right lene k liye.")
        # Your logic here...
        return []

class ActionStop(Action):
    def name(self) -> Text:
        return "action_stop"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Implement logic to stop the conversation
        dispatcher.utter_message("Okay, let's stop here.")
        # Your logic here...
        return []