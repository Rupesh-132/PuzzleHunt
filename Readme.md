## PuzzleHunt 
This is the puzzlehunt app where you can play tricky puzzle:


## App home page view:
- Any user with the email address can create account.
- After signup one can directly login(All the data is stored in the database(db.Sqllit3) is displayed at the admin portal(Django administration)
- The login session of he current user is saved and is not lost on refreshing the page
- Each page has the option to logout


![image](https://user-images.githubusercontent.com/79595858/236601976-d75dfab8-a999-4af7-9114-94dd79b68892.png)

## App link
https://web-production-ccad.up.railway.app/

## Following soft skill are assesed by this puzzle game
- Proficiency in Understanding english
- Logical ability
- Problem solving 
- Perseverence
- Patience
- Eye of detail
- Fact knowledge
- Knowledge of computer fundamentals(coding and decodoing)

## All the possible ways to solve the puzzle and the dead-ends should be documented for evaluation

# First Puzzle:
- This puzzle is easy, and can be solved by just reading the statement carefully and relating to real life
- It examines users eye of detail, knowledge of riddle understandng, solving picture puzzles.
 - The first clue will lead to a hint but the second hint just below is dead-end and will waste the time:
 - You need to come back to the riddle page and find another clue. Which is just below the floating waves at the bottom of the page;
 - The 3rd hint will lead you to the a picture based puzzle( you need to find the hidden words from them)
 - If you don' get it go to the next hint and you will get ans.
 - The ans is: Seed
 
 ## Note: You will not be able to solve the next puzzle until you solve first.
 
 # Second Puzzle:
 - This puzzle will examine:
  - Ability to understand the clue properly
  - Perseverence
  - Patience
  - Crossword puzzle solving ability(first clue will lead you there)
  - How much he understands the tricks where he got stucked into deadends
  - Similar dead-end is there but user need to choose between given crossword puzzles
  - Knowledge of facts as this fact is about tomato plant in canada.
  The ans is :tomato (which also appeared in the first question) in the picture;
  
  # Third Puzzle
 - This puzzle will test
  - logical ability
  - Knowledge of ascii
  - Abitily to observe things in the video(as hint)
  The ans is : C57099175B( All the letters at the even positions are encoded)
  
  # Fourth puzzle
  - This puzzle will judge:
   - Ability to understand the relation between hints
   - 6 qr codes has been given as hint ==> implying 6 letter word is there.
   - The ans will decoded from the first letter of the word that comes to the mind of player when he opens that link
   - The ans will be revere of the all the first letter of words you observe by going on the link
   - The ans is : Attire
  
 
## Steps to set up the project
- Made using Django framework.
- First model was build for the admin dashboard
- Admin portal to maanage login and signup sessions of the user
- Database set up using sqllit3
- Frontend design is done using Html, css, Javascript
- Questions can be posted from the admin portal.
- Login sessions is retained for a particular user who has logged in
- User will not be able to move to next question unless he solves current
- authentication of he user is done from the backend using django modules.
- Finally working project is deployed on railway.app(cloud hosting platform)

## Feature checklist
- Login using email and password: Yes
- User data(can be seen from admin dashboard): Yes
- Questions can be added from admin dashboard(customized) backened support
- Database support: Yes
- Login session retention : Yes
- Minimum 5 clues: Yes
- Minimum 2 Deadend: yes
- Restart feature on every page: Yes
- Logout feature at every page: Yes
- Music(if user try to submit empty ans: Yes
- ![image](https://user-images.githubusercontent.com/79595858/235852083-040c9e9e-e378-412d-99e9-e6234d725719.png)
- User can be added by the admin if he wants to
## Scope of improvement:
- Working on Ui to make it look classic;
- Working on leaderboard of each user
- Working on displaying graphs for all the actions of user(time sessions,correct ans, accuracy level)
