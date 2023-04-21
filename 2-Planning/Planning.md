# Planning

## What is planning?

Planning is the process of finding a sequence of actions that will lead us from a current state to a goal state.

A common example of planning is the calculation of driving directions to get to a destination. We'll use this example to illustrate the components of a planning problem below.

In order to plan, we need:

- A notion of of state - the street map and our position in it
- A start state - our initial position
- A goal - the position we want to reach
- A set of actions - drive left / straight / right at the next intersection
- Knowledge about how actions influence the state - If I drive straight at the next intersection, I will be at this position

A planning algorithm produces a sequence of actions that will transition us from the start state into a goal state. In our exampe, it tells us that we get to the destination by turning left, then right, then drive straight, then left again.
