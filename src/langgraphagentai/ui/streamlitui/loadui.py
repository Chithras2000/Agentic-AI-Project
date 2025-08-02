import os
import streamlit as st 
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagentai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config =  Config() # config are the configurations in the ui-dropdown values of each field
        self.user_controls = {}