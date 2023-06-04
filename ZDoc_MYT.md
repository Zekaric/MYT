
# Zekaric: Manage Your Tasks (ZMYT, My Tea, or Mighty)


## Table Of Contents

**1 - Summary**<br />
**2 - Install**<br />
**3 - Use**<br />

# 1 - Summary


My Tea is a simple task tracker as well as a simple web program.  The ideal is speed of entry and speed of keeping it all in order.

# 2 - Install


Copy the files to a folder.

Create an environment variable "MYT_DIR" where the files live.

Run from the command line or create a bat file with this inside it...

```
	python "%MYT_DIR%/myt.py"
```

In your browser go to...

```
	localhost:8000
```

You should now see the MYT interface.

# 3 - Use


Once installed you should have an empty data set.  There will be no projects and no task items.  You should be seeing the Projects page.  The title will be "Zekaric : MYT Projects".

There is a text field at the top with "New Project Name".  Enter a new project name in that field and hit enter.  The project should now show up in the list.  You can type a description in the blank field beside it if you want to provide some more information about the project.  Hit enter in the description field for your changes to be saved.  Similarly if you made a mistake in the Project name field you can correct it and then hit enter.

Project list will be alpha sorted always.  Project ID is used in the task storage to refer to the project a task belongs to.

"Go To Tasks" will take you to the task list.

The three white circle button and the 3 black circle button will turn the visibility of all projects on and off respectively.  You can click on an individual circle on a project line to turn that project on or off.  A black circle indicated on.  White is off.

In the Task list view the title of the page is "Zekaric : MYT Tasks"

"Go To Projects" will take you to the projects page.

The first column are the types of tasks and their visibility.  This task list is very software development centric.  In other words; you have work tasks, which means programming tasks.  Test tasks, writing unit tests and testing changes, QA.  Doc tasks, writing programmer and user documentation.  Rel tasks, whatever will be needed to release the product.  And Done which means the task is finished.

Each of these types can be shown or hidden by turning on or off their visibility.  Two convenient buttons at the top to turn them all off or all on in that order.

Next column shows all the projects you have defined.  You can turn certain projects off or on by click the circles.  The task list will refresh with those projects hidden from view or brought into view.

At the top of the task list is a pull down for the project to add to, followed by a field describing a new task.  Set your project, and type in the new task and hit enter.  The new task should appear in the list.  New tasks will also begin life as a "Work Todo" and minimum Priority and Effort.

The task list is always sorted based on project, status, priority, effort, and then id.  You may have to hunt for your new task unfortunately.

If you made a mistake on the project, adjust the task's project with the pulldown and the task will be assigned to that project you selected immediately.  This will mean it will change it's location in the list.

If you want to move the status of the task you can use the "<" and ">" buttons to move it to a previous state or to the next state in the lifecycle of a task.  The state order is "Work Todo", "Work In Progress", "Test Todo", "Test In Progress", "Doc Todo", "Doc In Progress", "Release Todo", "Release In Progress", and finally "Done" the end state.  Each state will have a different background color so that you can quickly see by it's color what stage the task is in.

You can also use the pulldown to pick the specific state for the task.

There is a convenient "Done" button to progress the task to the end state.  Done tasks will not have the "Done" button visible.

The circles under Pri(ority) and Eff(ort) columns are to give the task their level of importance (time sensitive, best next feature, most ciritical bug, etc.) and level of effort (how long a task will take to complete, how difficult that task will be, etc.)  There is a 6th circle under effort to indicate an unknown state.

The last "X" button on a line is to permanently remove the task from the list.
