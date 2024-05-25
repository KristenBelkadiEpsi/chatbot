from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCheckAvailability(Action):
    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        available = True  
        if available:
            dispatcher.utter_message(text="La date est disponible.")
        else:
            dispatcher.utter_message(text="Désolé, la date n'est pas disponible.")
        return []

class ActionBookTable(Action):
    def name(self) -> Text:
        return "action_book_table"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot('date')
        number_of_people = tracker.get_slot('number_of_people')
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')
        comment = tracker.get_slot('comment')
        
        reservation_id = "12345"
        dispatcher.utter_message(text=f"Votre réservation a été confirmée. Votre numéro de réservation est {reservation_id}.")
        return [SlotSet("reservation_id", reservation_id)]

class ActionCancelReservation(Action):
    def name(self) -> Text:
        return "action_cancel_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Votre réservation a été annulée.")
        return []

class ActionShowReservation(Action):
    def name(self) -> Text:
        return "action_show_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot('date')
        number_of_people = tracker.get_slot('number_of_people')
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')
        comment = tracker.get_slot('comment')
        dispatcher.utter_message(text=f"Voici les informations de votre réservation: Date: {date}, Nombre de personnes: {number_of_people}, Nom: {name}, Numéro de téléphone: {phone_number}, Commentaire: {comment}")
        return []

class ActionUpdateComment(Action):
    def name(self) -> Text:
        return "action_update_comment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        comment = tracker.get_slot('comment')
        
        dispatcher.utter_message(text=f"Le commentaire a été mis à jour: {comment}")
        return []

class ActionDailyMenu(Action):
    def name(self) -> Text:
        return "action_daily_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        daily_menu = "Voici le menu du jour: ..."
        dispatcher.utter_message(text=daily_menu)
        return []

class ActionAllergensList(Action):
    def name(self) -> Text:
        return "action_allergens_list"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        allergens_list = "Voici la liste des allergènes: ..."
        dispatcher.utter_message(text=allergens_list)
        return []

class ActionFullMenuLink(Action):
    def name(self) -> Text:
        return "action_full_menu_link"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        full_menu_link = "Voici le lien vers le menu complet: [URL du menu complet]"
        dispatcher.utter_message(text=full_menu_link)
        return []
