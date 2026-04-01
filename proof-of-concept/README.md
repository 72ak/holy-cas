# PROOF-OF-CONCEPT 1.0.0

This file contains documentation on mechanics, audio and GUI for the first iteration of my proof of concept.
All statements about "eventual" or "future" updates and additions are made with the assumption that this iteration of the proof-of-concept (or a variant thereof) is the one that is being run with.
THIS DOES NOT MEAN THAT THIS VERSION OR A VAIRANT THEREOF IS FINAL.

**THE AUDIO**
    - The game package comes with 1 audio file.
    - The audio file contains the game's music.
    - The audio is played using the playsound library.
    - To package the game executable with the audio file, run the following in the terminal:

    py -m PyInstaller --onefile --add-data "source/the rock n roll railroad.mp3;." source/PoC1.py

**THE GUI**
    - The GUI is built in Tkinter.
    - There is a main window which displays the buttons, the day, the time and also a silly catchphrase.
    - Each of the mechanics for the game has its own window, initialized using the following:

    <windowName> = tkinter.Toplevel()

    - There is also a ToolTip class that can be used when hovering above a pre-specified tkinter button. This is used in the "event" window but can be applied elsewhere.
    - The ToolTip class has two attributes. The button/element/widget, and the text to be displayed.

    class ToolTip:
        ...
    
    <buttonName> = tkinter.Button(<window>, <etc.>)
    tt = ToolTip(<buttonName>,<text:str>)

    Eventually, the buttons will almost definitely have some kind of graphic. Either the buttons will entirely be graphics, or will have graphics and some text to go with them.

    The backgrounds will also likely eventually have a background, something like a political office.

**THE MECHANICS**

Easily the longest bit right here, let me break it down.

    POLICIES:
        - Temporary
        - Change statistics about the government or the nation's resources
        - Some can be renewed.
        - The idea is also that things like money towards cultural programs, healthcare, education, etc. can also be changed here.
        - Areas of scientific study can also be taken as policies (e.g. "Modern Figher Jets" or "Improved Cancer Research.")
        - In a tkinter GUI, these policies should appear as buttons with tooltips. When clicked, or the tooltips are shown, the information and bonuses from the policy should be displayed.
        - Likely best defined in a class with some of the following attributes:
            - Duration:int
            - Effects:list(objects)
            - Renewable:bool
    
    ECONOMY:
        - Fairly self-explanatory
        - Shows resource output, national stock index,etc.
        - Use a graphing module in future to plot graphs of economy
        - Also where options around trade, tax and welfare can be chosen
    
    AFFAIRS:
        - World affairs!
        - Effectively just a news broadcast
        - Three different types: Broadcasting Company, Emergency Alert System and Cabinet.
        - Broadcasting Company: General news. Eventually, there will be decisions that can be made based on some bits of news. Kinda a gimmick, but keeps the game feeling dynamic.
        - Emergency Alert System: Emergency information. War? Famine? Rioting? Looting? Weather Events? All here. All of these events have actions that can be taken.
        - Cabinet: Political affairs. Someone in your cabinet leaves? One of your royal advisors has left their position? All in here. Sometimes, these actions will have decisions.

    IDEOLOGY:
        - My favourite bit (other than Focuses and Policies)
        - Allows you to change your government positions
        - Envisioned "slider" system to change particular aspects of government
        - Government ideology name changes based on sliders
        - EXAMPLE - modelling a Communist ideology with potential sliders:

        STATE OWNERSHIP                               PRIVATE CAPITAL
            O================================================

        NATIONALISM                                  INTERNATIONALISM
            =======O=========================================

        CULTURE                                        PROGRESS
            =================================O===============

        RELIGION                                       SCIENCE
            ================================================O

        - By changing the first slider more towards private capital and more towards religion, you might get something like a "National Socialist" position.

        - In this window, you can also change government type.
        - Change of government type can mean change in mechanics or capabilities
        - For example, changing from a "Republic" to a "Monarchy" replaces CABINET with ADVISORY, which can mean new opportunities for hiring, positions and focuses.

        - Changing all of this affects EVERY OTHER ASPECT OF THE GAME. POLICIES, ECONOMY, CABINET, FOCUSES, AFFAIRS AND MORE.

        - In future, music will also change if government type/system changes. For example, having a few themes for "Republic," "Monarchy," "Dictatorship," etc.
        - Additionally, in this window, players can view their party and nation's support for their ideology.

        - A FEW EXAMPLE IDEOLOGIES:
            - Communism
            - Hyper-conservatism
            - Hardline Capitalism
            - Eco-Facism
            - Nazism
            - Esoteric Facism
            - Revanchism
            - Theistic Ecological Socialism
            - Ultranationalism
            - Libertarianism
            - Social Liberalism
            - Socialism

        - A FEW EXAMPLE GOVERNMENT TYPES:
            - Monarchy
            - Republic
            - Constitutional Monarchy
            - Autocracy
            - Parliamentary democracy
            - Dictatorship
            - Papacy/Religious Counsel
            - Tribal Council
            - Scientific Community

    FOCUSES:
        - Focuses are semi-permanent "goals" for a government. They provide a permanent benefit to that government, so long as it maintains a government type or ideology that is compatible with that focus.
        EXAMPLE, USING PREVIOUS IDEOLOGY EXAMPLES:

        "Civil Liberties" - Generates +10 Culture points and also reduces SOCIAL and CABINET tensions by -0.01% every turn while this is in effect.
        COMPATIBLE TYPES:
            - Constitutional Monarchy
            - Republic
            - Parlimentart Democracy
            - Papacy
            - Scientific Community
        
        COMPATIBLE IDEOLOGIES:
            - Revanchism
            - Libertarianism
            - Social Liberalism
            - Socialism
        
        - If a government's type or ideology diverts from any of these, they lose the focus and the bonuses.
        - Likely best caluclated using a list to just scrape the total increases/decreases and apply them every new day.
        - These can also unlock new cabinet positions, affairs, events or policies.
    
    CABINET:
        - The government's structure.
        - Here, players can view the party support, tension, chance of defectors and new arrivals.
        - They can also assign different high-ranking roles, some of which are exclusive to certain government types or ideologies.

        EXCLUSIVE EXAMPLES:
            - Commissar for Public Works - Communism and Socialism-based ideologies.
            - Chancellor - Democratic government types
            - Commissar for War - Dictatorial types, socialism or communism-based ideologies OR nationalistic ideologies

        - If the overall cabinet support, number and roles falls below a certain threshold, the government collapses.

    NEW DAYS:
        - Every new day, the day changes (as do the dates. For the sake of simplicity thus far, each month only has 28 days (4 weeks). This will later change to reflect real time constructs.)
        - There is a 1 in 7 chance for an event to occur.
        - Catchphrase changes

    EVENTS:
        - Can vary. Could be press interviewers coming to talk to you, could be a government employee coming to discuss an important policy with you.
        - Gives options to act with popups explaining what they do.
        - Can affect policies, cabinet, ideology, economy or focuses.

