import pytest
from unittest.mock import Mock
from unittest.mock import patch
from project import generate_receipt
from project import email_receipt
from project import place_order
from table import table, order_list_headers
import project
import tkinter as tk

# patching a mock of email_receipt in order to test if generate_receipt attempts to call it
@patch("project.email_receipt")
def test_generate_receipt_calls_email_receipt(mock_email_receipt):
    # call generate receipt with parameters
    generate_receipt("smithycey@gmail.com", "Ciaran Smith")
    # asserting that generate receipt will call the mock of email_receipt
    assert mock_email_receipt.call_count > 0


def test_email_receipt_sends_mail():
    # asserting that email_receipt will return empty dict as smtp.sendmail returns
    # an dict containing the email addresses that failed to send if unsuccessful
    assert email_receipt("smithycey@gmail.com", 
                         "Ciaran Smith", 
                         table, order_list_headers) == {}



# patching a mock of generate_receipt, confirmation_window and clear_basket in order to test if place_order
# attempts to call them
@patch("project.clear_basket")
@patch("project.generate_receipt")
@patch("project.confirmation_window")
def test_place_order_calls_funcs(mock_confirmation_window, mock_generate_receipt, mock_clear_basket):
    # mocking function parameters
    mock_place_order = Mock()
    mock_place_order.checkout_window = tk.Toplevel()
    mock_place_order.first_name_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.first_name_entry = tk.StringVar(mock_place_order.checkout_window, "Ciaran")
    mock_place_order.surname_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.surname_entry = tk.StringVar(mock_place_order.checkout_window, "Smith")
    mock_place_order.house_num_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.house_num_entry = tk.StringVar(mock_place_order.checkout_window, "79")
    mock_place_order.street_name_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.street_name_entry = tk.StringVar(mock_place_order.checkout_window, "Beatrice")
    mock_place_order.town_city_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.town_city_enty = tk.StringVar(mock_place_order.checkout_window, "Walsall")
    mock_place_order.county_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.county_entry = tk.StringVar(mock_place_order.checkout_window, "West Mids")
    mock_place_order.post_code_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.post_code_entry = tk.StringVar(mock_place_order.checkout_window, "WS3 2AB")
    mock_place_order.phone_number_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.phone_number_entry = tk.StringVar(mock_place_order.checkout_window, "07908688714")
    mock_place_order.email_address_var = tk.StringVar(mock_place_order.checkout_window)
    mock_place_order.email_address_entry = tk.StringVar(mock_place_order.checkout_window, "smithycey@gmail.com")
    place_order(mock_place_order.first_name_var, mock_place_order.first_name_entry, 
                mock_place_order.surname_var, mock_place_order.surname_entry, 
                mock_place_order.house_num_var, mock_place_order.house_num_entry,
                mock_place_order.street_name_var, mock_place_order.street_name_entry,
                mock_place_order.town_city_var, mock_place_order.town_city_enty,
                mock_place_order.county_var, mock_place_order.county_entry, 
                mock_place_order.post_code_var, mock_place_order.post_code_entry,
                mock_place_order.phone_number_var, mock_place_order.phone_number_entry,
                mock_place_order.email_address_var, mock_place_order.email_address_entry, 
                mock_place_order.checkout_window)
    # asserting that the function successfully calls the mock confirmation_window function
    assert mock_confirmation_window.call_count > 0
    # asserting that the function successfully calls the mock generate_receipt function
    assert mock_generate_receipt.call_count > 0
    # asserting that the function successfully calls the mock clear_basket function
    assert mock_clear_basket.call_count > 0

