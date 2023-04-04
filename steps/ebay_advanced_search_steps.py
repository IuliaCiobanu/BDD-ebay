from behave import *

@when ("Home page: When I click on the advanced link")
def step_impl(context):
    context.advanced_search_object.click_advance_link()

@when("Advanced search page: I type '{item}' in the enter keyword textbox")
def step_impl(context,item):
    context.advanced_search_object.enter_keywords_or_item_number(item)

@when("Advanced search page: I select '{option}' from keyword options")
def step_impl(context, option):
    context.advanced_search_object.select_keyword_options(option)

@when("Advanced search page: I choose '{category}' from the category list")
def step_impl(context, category):
    context.advanced_search_object.select_search_category(category)

@when('Advanced search page: I click search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()

@then ("Home Page: I have at least '{results_no}' results returned")
def step_impl(context, results_no):
    context.advanced_search_object.expected_results(results_no)