
Here you can find some informal comments on the status of this package. Some features might be placed
into github-projects and issues, but they most likely will start here with a more informal description
of the feature.

## Current status

**28-nov-2019**

* The mujoco-backend is the only one integrated so far. I was rewriting the renderer from scratch (again)
  in the past month, so I couldn't port most of the working functionality on the bullet backend. During
  the integration of the new renderer, I also modified quite a bit the API exposed to the user, so most
  of the functionality for the bullet-backend has to be fixed to handle the new design.

* The funcionality in the bullet-backend prior to the whole rewrite mentioned above included support for
  agents working fully as in the mujoco-backend. There were still some issues with some agents, as I
  was starting to check how to handle some missing functionality in bullet, like damping and stiffness.

  Due to this mismatch, some models didn't simulate the same way, and some even had erratic behaviour.
  One such case was the mjcf-humanoid, as it seems it relays heavily on damping, and it also is one of
  the models that has 2-3 joints per link in most links, which seems to not work nicely with the approach
  I took to handle bullet's Featherstone implementation. I'll fix these issues and work on adding support
  to at least some required functionality to have an even more similar behaviour to the mujoco-backend (kind
  of reverse engineer the current models in pybullet, to check how they handle some models like the humanoid).

* The renderer has been integrated into the core library, and fixes most of the issues I had with the
  previous iteration of the renderer: weird lighting, low fps in some cases, ... . I also added a bunch
  of required functionality: blending, instanced debug draws, render targets (to simulate camera sensors),
  proper imgui integration, culling, ... . Once I finish porting from the bullet-backend, I'll give some
  time to the headless renderer, as it will become a must once fellow researchers start using it with
  camera sensors.

