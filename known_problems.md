## Known problems

- [x] ~~db gets called everytime we want to get task info, which makes app slow~~
solved this by loading db at the start

- [x] ~~if a task gets deleted (except for last task in data), get_task_by_id wont work~~
\
solved this by setting task to deleted

- [x] ~~cant create a task with /api/tasks/create~~