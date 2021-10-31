# Analysing working memory using foraging tasks

Foraging is one of the basic tasks that animals perform in the wild that requires the use of working memory.

This repo consists of :  

`pyschopy tasks` where there are two preliminary version of foraging tasks. 
1. `aperture_search.py` contains a task where the participant is unaware of the environment and has to explore to find the location of the berries in the patch using mouse cursor. A circular aperture is only visible to the participant when exploring for harvesting. When the participant clicks on the berry, the reward reduces and they have to wait for 5s until they can move to the next patch for harvest. The wait time at each patch is introduced to mimic harvest time in real case scenarios. The hypothesis is that this task involves the utilisation of working memory to keep track of the berries in the patch while exploring as well as the the reducing reward after every harvest. 
2. `mouse_click.py` contains a task where the particpant has access to information about the number of berries present in the patch and the location of an avatar of a man that could forage these berries. On mouse click on one of the patches, the avatar reaches the berry to harvest. Here, the travel time is included proportional to the distance between the avatar and the clicked berry.

`ForagingByRL` has a reimplementation of a simple reinforcement Q learning agent learns to avoid toxic predators and choose the non-toxic ones by exploration based on the paper "The application of temporal difference learning in optimal diet models, Teichmann et. al,2013". The summary and paper is present in `paper summary` folder. The Q-learning based approach with soft-max policy used in the paper is used as an inspiration for the reinforcement learning agent used to compare human participants performing the foraging tasks. The reinforcement learning agent in this case would have to choose for rewarding berry bushes compared to non-rewarding ones.
    
`Analysis` folder has all the code, plots, data and analysis obtained for mouse_click.py task.

More work needs to be done on large scale participants. 