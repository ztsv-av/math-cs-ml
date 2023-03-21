# Object‐Oriented Systems Analysis and Design (OOSAD)

One of the categories of information systems development methodologies is object‐oriented analysis and design. Object‐oriented approaches to developing information systems, technically speaking, can use any of the traditional methodologies. However, the object‐oriented approaches are most associated with a phased development RAD. The primary difference between a traditional approach like structured design and an object‐oriented approach is how a problem is decomposed. In traditional approaches, the problem‐decomposition process is either process‐centric or data‐centric. However, processes and data are so closely related that it is difficult to pick one or the other as the primary focus. Based on this lack of congruence with the real world, new object‐oriented methodologies have emerged that use the RAD‐based sequence of SDLC phases but attempt to balance the emphasis between process and data by focusing the analysis of problems on objects that contain both data and processes.

According to the creators of the Unified Modeling Language (UML), Grady Booch, Ivar Jacobson, and James Rumbaugh,5 any modern object‐oriented approach to developing information systems must be use‐case driven, architecture‐centric, and iterative and incremental.

### Use‐Case Driven

Use‐case driven means that use cases are the primary modeling tools defining the behavior of the system. A use case describes how the user interacts with the system to perform some activity, such as placing an order, making a reservation, or searching for information. The use cases are used to identify and to communicate the requirements of the system to the programmers who must write the system. Use cases are inherently simple because they focus on only one business process at a time. In contrast, the process model diagrams used by traditional structured and RAD methodologies are far more complex because they require the systems analyst and user to develop models of the entire system. With traditional methodologies, each system is decomposed into a set of subsystems, which are, in turn, decomposed into further subsystems, and so on. This goes on until no further process decomposition makes sense, and it often requires dozens of pages of interlocking diagrams. In contrast, a use case focuses on only one business process at a time, so developing models is much simpler.6

### Architecture‐Centric

Any modern approach to systems analysis and design should be architecture‐centric. Architecture‐centric means that the underlying software architecture of the evolving system specification drives the specification, construction, and documentation of the system. Modern object‐oriented systems analysis and design approaches should support at least three separate but interrelated architectural views of a system: functional, static, and dynamic. The functional, or external, view describes the behavior of the system from the perspective of the user. The structural, or static, view describes the system in terms of attributes, methods, classes, and relationships. The behavioral, or dynamic, view describes the behavior of the system in terms of messages passed among objects and state changes within an object.

### Iterative and Incremental

Modern object‐oriented systems analysis and design approaches emphasize iterative and incremental development that undergoes continuous testing and refinement throughout the life of the project. This implies that the systems analysts develop their understanding of a user's problem by building up the three architectural views little by little. The systems analyst does this by working with the user to create a functional representation of the system under study. Next, the analyst attempts to build a structural representation of the evolving system. Using the structural representation of the system, the analyst distributes the functionality of the system over the evolving structure to create a behavioral representation of the evolving system. As an analyst works with the user in developing the three architectural views of the evolving system, the analyst iterates over each of and among the views. That is, as the analyst better understands the structural and behavioral views, the analyst uncovers missing requirements or misrepresentations in the functional view. This, in turn, can cause changes to be cascaded back through the structural and behavioral views. All three architectural views of the system are interlinked and dependent on each other (see Figure 1‐2). As each increment and iteration is completed, a more‐complete representation of the user's real functional requirements is uncovered.

![image](https://user-images.githubusercontent.com/73081144/176342785-b7aabd2e-8a8d-4adb-bc17-c9699da6c774.png)

## Benefits of Object‐Oriented Systems Analysis and Design

Concepts in the object‐oriented approach enable analysts to break a complex system into smaller, more‐manageable modules, work on the modules individually, and easily piece the modules back together to form an information system. This modularity makes systems development easier to grasp, easier to share among members of a project team, and easier to communicate to users, who are needed to provide requirements and confirm how well the system meets the requirements throughout the systems development process. By modularizing systems development, the project team actually is creating reusable pieces that can be plugged into other systems efforts or used as starting points for other projects. Ultimately, this can save time because new projects don't have to start completely from scratch.