
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

**16-dec-2019**

* The functionality for single-body objects is working in all branches (MuJoCo, DART, Bullet and RaiSim). I haven't updated
  the docs yet as I'm currently working on Compound-bodies as well (to create more complex structures like doors, etc.), and
  I'd like to have at least that working on MuJoCo as a proof of concept (sorry for that, I should have started working on that
  on a separate branch). Single-bodies support both primitives like spheres, boxes, etc., meshes, and also height fields (so we
  can in principle start building some nice terrain using these). There's still some support that I have to make sure is exposed
  in all backends, like collision groups, changing collider sizes at runtime, etc.. I'll keep posting in the next couple of
  weeks.
* Note that Compound-bodies are different from Kinematic trees, as the later is the abstraction that will be used for agent
  in the environment (will have actuators, sensors, and more functionality). Currently there's a proof of concept working on
  MuJoCo based on an old API that I designed, but I'll reimplement all that from scratch to make sure everything works correctly
  and makes sense in all backends.
* Just to clarify, the **demo** that's currently working **shows the proof of concept for a single backend (MuJoCo)**. Some of
  the functionality is not standard yet, as I'm currently changing the API a lot to expose common functionality to all backends.
  The timeline for the next month includes finish full support for single bodies, compounds, and kinematic trees (agents) working
  in all backends, so the demo should then work in all backends as in the gif shown in the readme.
* Finally, if you'd like to have a feature implemented, just let me know as I'm currently designing most of the core 
  functionality and the API, so perhaps I could accommodate this into the current timeline I have. Just send me an email to
  wpumacay@gmail.com, I'd be happy to discuss your requirements.
