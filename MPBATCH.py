r"""
Program Purpose: A Python Template for a Streamlit multipage app".
Topic: This creates a webpage with:
        - A vertical page navigation tool bar on the left.
        - A right side panel at which displays different pages.
          - The right panel pages are  streamlit 'batch' form pages
            with a streamlit form_submit_button.
Author: 
"""

# TO DO:


# streamlit run "G:\My Drive\UConn\1-Subjects\Python\STAT476\CODE\StreamlitMultipageBatchForm\MPBATCH.py"
import streamlit as st
from streamlit import session_state as S
import os
import random
import numpy as np
import pandas as pd

# Plotly imports. Some may be flagged as unused, but import them anyway.
import plotly
import plotly.express as px       # We tend not to user plotly express.
import plotly.graph_objects as go # We prefer Plotly graph object.

class Global_Variables():  # A class creating all global variables.
      placeholder = None
# End of class Global_Variables.      
G =  Global_Variables()    # Instantiate the global variables.    

def MainLine():
    # On first program load initialize the static area and session state.
    if "RequestedPage" not in st.session_state:
        S.RequestedPage = "HomePage"
        Initialization_Perform_First_Load_Only()
        Menu_Build()
        HomePage_Build_And_Show()
    else:
        # We are responding to a user input.
        Menu_Build()
        # Select the requested page.
        if  S.RequestedPage == "HomePage":     HomePage_Build_And_Show()
        elif S.RequestedPage == "Plot1Page":   Plot1Page_Build_And_Show()
        elif S.RequestedPage == "Plot2Page":   Plot2Page_Build_And_Show()
        elif S.RequestedPage == "ContactPage":  ContactPage_Build_And_Show()
        else: st.stop("Error: 1200. Please report program error")   
    return() # End of function: MainLine.


def Menu_Build():
    # Our menu in a vertical toolbar on the left of the page.
    with st.sidebar:
        st.success("STREAMLIT APP.  \r BATCH FORM DEMONSTRATION ") # App Title
         
        # Add Page selection buttons.
        st.button("Home", on_click=Homepage_CallBack,
                  help="Go to the home page.")
        st.button("Plot1Page", on_click=Plot1Page_CallBack,
                  help="Create and display Plot1.")
        st.button("Plot2Page", on_click=Plot2Page_CallBack,
                  help="Create and display Plot2.")
        st.button("Contacts", on_click=ContactPage_Callback,
                  help="Contact the folks at IBM.")   
        st.write("_____________________________________")
    return()



def HomePage_Build_And_Show():
    fn = os.path.basename(os.path.abspath(__file__)).upper()
    st.subheader(f"🟢 WELCOME TO THE HOME PAGE OF APP '{fn}'.")
    
    st.info("🟢 "
        "THIS PAGE IS CONSTRUCTED AS A STREAMLIT 'BATCH PAGE' AND A "
        "SINGLE 'form_submit_button'.  \r"
        "A batch page has the advantage that "
        "a user input form can be completely filled out before "
        " submitting. This prevents every user change to  "
        " widgets from reinvoking the app.  \r"
        " But forms  don't allow any other buttons.  "
        " The streamlit_download file button works if placed outside the "
        " form but this can be awkward and will clear the current plot"
        " when used."
        "This could be a real drawback.  \r   \r"
        "SEE 'MPNOBATCH.py' FOR AN EXAMPLE OF THIS APP  N O T  USING A " 
        "STREAMLIT FORM WHICH WILL:(a) ALLOW ANYTHING ON A PAGE AT "
        "THE EXPENSE OF A LITTLE LESS EFFICIENCY (b) HAVE INSTANT UPDATES "
        "OF THE DISPLAY AS WIDGETS CHANGE.  ")
 
            
def Plot1Page_Build_And_Show():
###############################################################################    
######### +++ BUILD THE USER INPUT PANEL.    
    st.subheader("🟢 WELCOME TO THE Plot1Page PAGE OF APP.  ")
    

    # Make the streamlit fullscreen  icon larger.   
    Streamlit_FullScreenIcon_Format() 

    # - We now make the right panel a single form with a single submit button.
    #   Because we are using the Streamlit "form" and its form_submit_button,
    #   this app only reruns when you hit the form submit button, NOT 
    #   (as is default behavior) at each widget interaction.
    Plot1Form = st.form(key="Plot1Form", clear_on_submit=False)

    with Plot1Form:
###################### CREATE A PANEL OF INPUT WIDGETS ########################
        st.info("Please supply the plots'  parameters and click 'PLOT NOW'.")
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            P1DemoVar1=st.number_input(label="X",
              min_value=0,max_value=100,step=1,value=0,
              format="%i", # Integer field.
              help="""INTEGER: X [0,100] but can't be 99. """ ) 
            P1DemoVar5=st.number_input(label="P1DemoVar5",
              min_value=1,max_value=1000,step=1,value=100,
              format="%i",
              help="""INTEGER: P1DemoVar5 can't be 99. """ ) 
        with col2: 
            P1DemoVar2=st.number_input(label="P1DemoVar2",
              min_value=1,max_value=1000,step=1,value=100,
              format="%i",
              help="""INTEGER: P1DemoVar2 can't be 99. """  ) 
            P1DemoVar6=st.number_input(label="P1DemoVar6",
              min_value=1.0,max_value=1000.0,step=1.0,value=23.45,
              format="%f", # Float field.
              help="""FLOAT P1DemoVar6 can't be 99. """ )
        with col3: 
            P1DemoVar3=st.number_input(label="P1DemoVar3",
              min_value=1.0,max_value=1000.0,step=1.0,value=900.0,
              format="%f",
              help="""FLOAT: P1DemoVar3 can't be 99. """ ) 
        with col4: 
            P1DemoVar4=st.radio(
                label="'P1DemoVar4'. What's your favorite movie genre",
                options=('Comedy', 'Drama', 'Documentary'),
                index=1,
                help="A demonstration of a streamlit radio button input.")        
        
        # Add a form submit button.
        # Every "form" must have exactly one form_submit_button.
        if Plot1Form.form_submit_button(label="PLOT NOW"):
    ######## VALIDATE THE USERS INPUT #########################################
            if P1DemoVar1 == 99:
                msg = "ERROR 23: P1DemoVar1 cannot be 99."
                st.error(Msg_Set(msg))  # Show the error in an error box.
                return()
    
            if P1DemoVar2 == 99:
               msg = "ERROR 23: P1DemoVar2 cannot be 99."
               st.error(Msg_Set(msg))  # Show the error in an error box.
               return()
    
             # If we fall through here the users input is valid. 
         
        else: # Form button not pushed.
            # If this is the first time through or the user has clicked
            # a download button a reload of the app occurs.
            # In those cases we don't want to display or redisplay
            # the plot so we return here. We only show the plot if
            # the user has clicked the form "Go" button.
            return()
        
    # If we fall through here the users input is valid. 
    
###############################################################################
#        IF WE FALL THROUGH HERE THE USER HAS CLICKED THE "GO" BUTTON AND     #
#        AND THE USER INPUT IS VALID                                          #
############################################################################### 

########  PROCESS THE USERS INPUT. BUILD TABLES ETC READY TO PLOT #############

    #++++++++ CREATE A DATATABLE BASED UPON THE USERS INPUT.  
    # The DataTable is a pandas dataframe (data table) to store our results.
    x = list(range(P1DemoVar1, P1DemoVar1+100))
    y1 = x
    y2 = [item ** 1.2 for item in x]
    y3 = [item * -1 for item in x]
    
    # Create an example Pandas dataframe from the users input.
    # We will generate our plots from this DataTable.
    DataTable= pd.DataFrame()
    i = -1
    for  xvalue in (x):
        i = i + 1
        newrow = {"x" : xvalue,
                  "y1":   y1[i],
                  "y2":   y2[i],
                  "y3":   y3[i],
                  "sum of y1 and y2 ": y1[i] + y2[i],
                  "sum of y1 , y2 and y3": y1[i] + y2[i] + + y3[i],
                  "randomInt": random.random(),
                  "randomFLoat": random.randint(1,100) 
                }
        DataTable = DataTable.append(newrow, ignore_index=True)

###############################################################################
##############  DISPLAY A PLOT REPORT/TITLE BOX ON THE GUI  ###################


    Plot_Report =  (
        "A Report on the users input used to make the plot.  \r" +
        "AT THE MOMENT THERE IS NOT MUCH RELATIONSHIP BETWEEN THE INPUT "
        "AND OUTPUT.  \r Only input X is used to generate the plot.  \r "
        "THIS IS JUST A ROUGH DEMONSTRATION OF STREAMLIT "
        "BASICS.  \r"
        f"X = {P1DemoVar1:,}     \r"           +
        "y1 = X        \r"                     +
        "y2 = X ^ 1.2  \r"                     +
        "y3 = X ^ -1  \r"                      +
        f"P1DemoVar2 = {P1DemoVar2:.4f}   \r"  +
        f"P1DemoVar3 = {P1DemoVar3:.4f}   \r"  +
        f"P1DemoVar4 = {P1DemoVar4}   \r"      +
        f"P1DemoVar5 = {P1DemoVar5:.5f}   \r"  +
        f"P1DemoVar6 = {P1DemoVar6:.6f}   \r"      )
    
    # For streamlit.text use spacespace\n. For streamlit.info use spacespace\r
    # In this case we are using a st.text box so change the eol character.
    Plot_Report = Plot_Report.replace("  \r", "  \n")
    
    with Plot1Form: 
         with st.expander(label="PLOT REPORT", expanded=False):                                                      
              st.text(Plot_Report) # Show the plot report. 
    

###############################################################################
############# BUILD AND DISPLAY THE PLOT USING OUR PREPARED DATA  #############    
## We use plotly not matplotlib to create the plot. Plotly gives fantastic
## interactive plots under streamlit. Matplotlib is only static under 
## streamlit.
## We use Plotly GO (Graph objects) not plotly ex (Express).
## Plotly go is more work but it gives you control over how the details are
## displayed. Plotly express is quick but you have less control.

    Fig1 = go.Figure() # Create an empty Plotly figure.
    
    # Add all graph lines (aka traces) on one figure.
    Fig1.add_trace(go.Scatter(
        name="Y1 Value = x", # Shows in Legend.
        text="Y1", # Shows in Hovertext.
        legendrank=1, # Where the line will appear in the legend list.
        x=DataTable["x"], y=DataTable["y1"], 
        visible=True,
        mode="lines",
        line=dict(color="red")  )) 
   
    Fig1.add_trace(go.Scatter(
        name="Y2 Value = x ^ 1.2", # Shows in Legend.
        text="Y2", # Shows in Hovertext.
        legendrank=1, # Where the line will appear in the legend list.
        x=DataTable["x"], y=DataTable["y2"], 
        visible=True,
        mode="lines",
        line=dict(color="blue")  ))     

    Fig1.add_trace(go.Scatter(
        name="Y1 Value = x ^ -1", # Shows in Legend.
        text="Y3", # Shows in Hovertext.
        legendrank=1, # Where the line will appear in the legend list.
        x=DataTable["x"], y=DataTable["y3"], 
        visible=True,
        mode="lines",
        line=dict(color="green")  )) 

    # Adjust titles, grid, font etc.
    Fig1.update_layout(title="<b>Demonstration Interactive Plotly Plot",
                       title_x=0.4)
    Fig1.update_layout(xaxis_title="<b>X Axis Title")
    Fig1.update_layout(yaxis_title="<b>Response Variables")
    Fig1.update_xaxes(showgrid=True,gridcolor="lightgray")
    Fig1.update_yaxes(showgrid=True,gridcolor="lightgray")
    
    # We MUST LET THE STREAMLIT WEB PAGE AUTOSIZE so that it will
    # will adjust automatically to fit different size screens."
    # DON'T  use any width and height paremeters on plots or
    # any other feature that sets an absolute size for anything.
    Fig1.update_layout(autosize=True, width=None, height=None) #800*1100
    Fig1.layout.plot_bgcolor = "white"
    Fig1.layout.margin = dict(t=5, b=5, l=0, r=0)
        
    # Adjust the hover text aka "mouseover" text.
    Fig1.update_layout(hovermode="x") # "x", "x unified" or "closest"
    # Show vertical and horizontal hover axes intersect lines.
    Fig1.update_xaxes(showspikes=True, spikecolor="green",spikethickness=1, 
                        spikesnap="cursor", spikemode="across")
    Fig1.update_yaxes(showspikes=True, spikecolor="green", spikethickness=1)

    # Adjust the axes tick marks.
    Fig1.update_layout(xaxis=dict(tickmode='linear',tick0=0, dtick=10))
    Fig1.update_layout(yaxis=dict(tickmode='linear',tick0=0, dtick=50))
  
    # Specify what is shown on each hovertext line.
    # https://plotly.com/python/hover-text-and-formatting/#advanced-hover-template
    HT=("<br>" + "X Value=%{x:.4f},  " + "Response Value=%{y:.4f}") 
    Fig1.update_traces(hovertemplate=HT)
    # Adjust the hovertext font.  
    Fig1.update_layout(hoverlabel=dict(font_size=12,bgcolor="palegreen")) 
  
    # Adjust the legend.
    Fig1.update_layout(legend_title_text="<b>Legend.")
    Fig1.update_layout(
    legend=dict(
        # title_font_family="Times New Roman",
        font=dict(size=10),
        # Make the legend transparent to minimize its obscuration of the plot.
        bgcolor="rgba(0,0,0,0)", 
        bordercolor="Black",
        borderwidth=1 ))
    # Place the legend at a desired location on the plot.
    # The legend will sometimes obscure the plot.
    # So we place it to the right of the plot.
    # The location of the legend reduces and reshapes the plot display itself.
    # Fortunately the Plotly "full screen" option can be used to view the plot
    # beautifully.
    Fig1.update_layout(
      legend={"yanchor":"middle","y":+ 0.50,"xanchor":"right","x":+1.35})
    
    # Add border around the plot. #,ivory,linen,mintcream,snow,whitesmoke
    Fig1.update_layout(margin=dict(l=10,r=10,t=30,b=30),
                       paper_bgcolor="mintcream" ) 
    Fig1.update_xaxes(showline=True,  linecolor='black', mirror=True)
    Fig1.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)
           
    with Plot1Form: # Place plot on the web page. 
        st.plotly_chart(Fig1, use_container_width=True)  

###############################################################################
######## SHOW THE DATA TABLE ON PLOT1 PAGE  ###################################
    with Plot1Form: 
       st.info("🟢 THE DATA TABLE GENERATED BY YOUR PARAMETERS FOLLOWS.")
    
    # Place the datatable on the page.
    with Plot1Form: 
        st.dataframe(data=DataTable, width=None, height=None)

###############################################################################
    #  +++ ADD A "DOWNLOAD" DATAFRAME BUTTON.
    # NOTE: IF CLICKED THIS BUTTON WILL RESET THE FORM.
    #  We are using a streamlit batch form which only allow one button,
    #  that is, the "form_submit button".
    
    # So this button is outside the form and if clicked will do the
    # job of downloading the file but it will also reset the 
    # form and clear all inputs and plots.
  
    # Convert the data frame to an "internal" csv file.
    DataFrame_CSV = DataTable.to_csv().encode('utf-8')
    DataTableFileName = "Plot1DataTable.csv"
    helpstr = f"""You can save the data frame to your computer using 
        this button.  \r
        The file will be called {DataTableFileName}.   \r
        The file will be in CSV format, (Comma Separated Variable).   \r
        The file will be saved in your browser's default download location
        on your computer.  \r
        There will be no "save as" menu. The file name is hard coded.  \r
        Using this feature will reset your plot.  \r
        You can enlarge the table by clicking the 'View fullscreen' icon
        located at the top right of the table.  \r
        'Float' the mouse over the table and the 'View fullScreen'
        icon will appear.
         """
    st.download_button(label="⚙️ Download The DataFrame", 
                      data=DataFrame_CSV, 
                      file_name=DataTableFileName, 
                      mime= "text/csv",
                      key="DownloadCSV_Button", 
                      help=helpstr, 
                      on_click=None, 
                      args=None,
                      kwargs=None, 
                      disabled=False)

    return() # End of function: Plot1Page_Build_And_Show


def Plot2Page_Build_And_Show():
    
######### +++ BUILD THE USER INPUT PANEL.    
    st.subheader("🟢 WELCOME TO THE Plot2Page PAGE   \r"
            "Nothing here yet.")
    return() # End of function: Plot2Page_Build_And_Show

def ContactPage_Build_And_Show():
    st.subheader("🟢 WELCOME TO THE CONTACTS PAGE   \r"
            "Nothing here right now.")
    return() # End of function: ContactPage_Build_And_Show


def Initialization_Perform_First_Load_Only():

    # +++ Initalize variables etc.
    Initialization_Perform_EveryRun()
   
    # ++++ Set up a typical "About/Help" menu for the webpage.

    
    # +++ DETAILS ABOUT THIS MODULE
    ThisModule_Project = "My project."
    ThisModule_Version = "Version 01. 2022 March 16."  
    ThisModule_Author = "Author would appear here."
    ThisModule_Purpose = ("To demonstrate a Streamlit multipage app using "
                          "a streamlit 'Batch' form and form_submit_button. ")
    ThisModule_Contact = ("Contacts would appear here.")
    ThisModule_Legal = ("legal would appear here.")
    ThisModule_Docstring = (__doc__)
    ThisModule_FullPath  = os.path.abspath(__file__)
    ThisModule_FileName = os.path.basename(ThisModule_FullPath)
    ThisModule_ProjectPath = os.path.dirname(ThisModule_FullPath)
    # Link to APP documenation at github.
    Link01 = "https://www.ibm.com/us-en?ar=1"  
    # Link to project repository at github.
    Link02 = "https://www.ibm.com/us-en?ar=1" 
    # Link to APP Code at github.
    Link03 = "https://www.ibm.com/us-en?ar=1" 
    # Link to report a bug.
    Link04 = "https://www.ibm.com/us-en?ar=1"  
    
    # Add this information to the web page "help" and "about" menus.
    #  - The set_page_config command can only be used once per run.
    #  - The set_page_config command be the first Streamlit command used.
    #  - New line marker \n must be preceeded by at least two blanks to work.
    st.set_page_config  (
        # Add a short title that will show in the browser tab header.
        page_title = "Webpage Header. ", 
         
        page_icon = "😅",
         
        layout="centered", # or "wide".
            # 'wide' gives a bigger display. 
            # 'centered' gives a smaller display
            #  Remember that plots and tables etc on the streamlit webpage 
            #  can be "blownup" by the user clicking an "expand" icon.
            #  So don't worry if the normal view is too small.
         
        initial_sidebar_state="auto",
         
         # \r requires two preceeding spaces to work.
        menu_items={ # These appear as the webpage "about" menu items.
        'Get Help  ':  Link01,
        'Report a bug  ': Link04,
        'About': '  \rProgram: '            + ThisModule_FileName 
               + '  \rVersion:  '           + ThisModule_Version 
               + '  \rProject:  '           + ThisModule_Project
               + '  \rProgram Purpose:  '   + ThisModule_Purpose 
               + '  \rAuthor:  '            + ThisModule_Author   
               + '  \rLegal:  '             + ThisModule_Legal
               + '  \rContact:  '           + ThisModule_Contact
               + '  \rApp Documentation:  ' + Link01
               + '  \rCode:  '              + Link03
               + '  \rProject Files:  '     + Link02
                  }
                         )
    # End of st.set_page_config 
    
    # Make the streamlit fullscreen  icon larger.   
    Streamlit_FullScreenIcon_Format() 
    
    
    # +++++  Create Static variables.
      # No extra static variables required at the moment.
    
    # +++++ Put here any other "first run" initialization.
     # No extra initialization required at the moment.


    return()  # End of function: Initialization_Perform_First_Load_Only

def Initialization_Perform_EveryRun():
    return()  # End of function: Initialization_Perform_EveryRun

    


################# U T I L I T Y   F U N C T I O N S ########################## 

def Homepage_CallBack():
    S.RequestedPage = "HomePage"  # Update the current page state.
    return()

def Plot1Page_CallBack():
    S.RequestedPage = "Plot1Page"
    return()

def Plot2Page_CallBack():
    S.RequestedPage = "Plot2Page"
    return()

def ContactPage_Callback():
    S.RequestedPage = "ContactPage"
    return()

def Msg_Set(TextString):
    FormattedText = TextString
    ErrStr = TextString[0:5].upper()  
    if ErrStr == "ERROR":
       FormattedText = ("❌  There is an error in your input.  \r"
                       f"{FormattedText}  \r  Please correct and try again.")
    return(FormattedText)    


def Streamlit_FullScreenIcon_Format():
    # This increases the visibility of the Streamlit 'full page' icon.
    style_fullscreen_button_css = """
         button[title="View fullscreen"] 
         {background-color: #004170cc; left: 2; color: white; }
    
         button[title="View fullscreen"]:hover 
         {background-color: #004170; color: white; } """
    
    st.markdown( "<style>" 
                + style_fullscreen_button_css
                + "</styles>",
                unsafe_allow_html=True,
               ) 
    return()  # End of function: Streamlit_FullScreenIcon_Format 
    
def ConsoleClear(): # Clear all output in console.
    try:     # This works regardless of Operating System prevailing.
        from IPython import get_ipython
        get_ipython().magic("clear")
        get_ipython().magic("reset -f")
    except:
        pass
    return()  # End of function: Console_Clear 

def Validate_Float(TextString):
    try:
        tempvar = float(TextString)
    except:
        return (0,False)
    else:
        return(tempvar,True)

def Validate_Integer(TextString):
    try:
        tempvar = int(TextString)
    except:
        return (0,False)
    else:
        return(tempvar,True)



MainLine()  # Start the program