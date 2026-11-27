''' 
functions for json file which stores temporary session information
if the site would be excited in the middle of adding a new session
therefore each batch of exercises is added incrementally to this temp json, if applicable
'''
import supabase_utils.file_handling as sb_fh
import streamlit as st
import json

PATH = "data/temporary_session_data.json"

NAME = "workout-data"

def load_temp_session_data():
    '''wrapper for the file download in supabase utils'''
    return sb_fh.download_data_from_supabase_bucket(PATH, NAME)

def write_temp_session_data(data):
    '''wrapper for the file upload in supabase utils'''
    sb_fh.upload_data_to_supabase_bucket(data, PATH, NAME)

def temp_data_status():
    return; # TODO
