
# Initial concept
My initial idea for this game, I wrote down here on July 29th:

“Idea: A game based on The Little Prince
-Explore the planets he has visited
-When you click the planet, there will be some info on the inhabitant and a picture
-some (planets)feature small mini-games”

# Initial research
There were a few things I knew I would need for my project, and I found amazing tutorials on the internet.

baraltech.(2022, February 5). HOW TO MAKE A MENU SCREEN IN PYGAME! [Video]. 
YouTube.
https://youtu.be/GMBqjxcKogA?si=j9aEOwYKxDblbSdb
baraltech. (2021, April 21). EASY Way to Make BUTTONS for Python/PyGame 
Projects [Video]. YouTube
https://youtu.be/al_V4OGSvFU?si=F_X6BXgxhK1LjW6y 
Coding with Russ. (2022, March 31). PyGame Beginner Tutorial in Python - 
Infinite Scrolling Background [Video]. YouTube
https://youtu.be/ARt6DLP38-Y?si=fiX1MC3DTYP_zzRy
Jagadeesan, U.R. (2024). Building a Whack-a-Mole Game with Python and 
Pygame. Medium
https://medium.com/@uva/building-a-whack-a-mole-game-with-python-and-
pygame-264c9f4cd512 

# Development process
For the most part, I stuck with the initial idea. 
I started with a menu screen that featured a start and quit button, as well as a dynamic scrolling background. To make the menu possible, I first built a Button class, which I was then able to reuse for the main menu and later also for the mini-game button. This was one of the first times I actually saw the benefit of writing code in a reusable way.

Since I also knew I would be repeating a similar layout on the planet screens, I made a base Planet class that handled the main loop, event handling, drawing, and the ESC instructions. That meant the subclasses only had to focus on their unique parts, like image and text.

From there, I built the universe with the different planets and tried to expand on what we learned in class. For example, I used collision detection and arrow key movement to handle player navigation in the universe. Thanks to the Planet base class, each planet is linked to its own subclass. 

When I had most of the planets ready with their text and picture, I had my parents playtest the game. I realized how important it is to have other people test your game as things that were obvious to me were confusing to them, like whether to use the arrow keys or the mouse. Based on their feedback, I added instructions to the main menu for clarity.

This project was especially meaningful to me because The Little Prince is one of my favorite books. It helped me through some tough times, and working on something I'm passionate about made it a lot more fun to work on and easier to overcome challenges. 

# Challenges:
During development, I faced several challenges:


-Figuring out how to use many different py files and classes together
-Struggling more than expected with the mini-game button, which I thought would be an easier part, since I already had my button class and also made the main menu buttons.
-In general, I think I was a little too optimistic when I said the game should feature multiple mini games and really underestimated how complex the overall project actually turned out to be.
-The unexpected complexity of the game is also why the mini-game turned out fairly simple at the end
-I didn’t realize my project was missing .gitignore until weeks after starting, and accidentally committed unnecessary files. This taught me how important it is to set the project up properly from the start.


# Future improvements and limitations
-The game currently only includes one mini-game
-After visiting a planet, the prince currently always returns to the Lamplighter’s planet
-At first, I didn't commit to GitHub often enough. I improved on this later, but I know I can do even better.
-It would be great to expand the mini-game - highscore/win/lose system?
-The planets could be more interactive with dialogue or other things.
-Even with the planet base class, there was still some repeated code (like the draw_multiline_text method).




# References
Saint-Exupéry, A. d., & Woods, K. (1982). The little prince. Harcourt Brace Jovanovich.
