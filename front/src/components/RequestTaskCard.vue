<template>
  <div class="task-card">
    <span class="task-card-empl">{{ employee }}</span>
    <span class="task-card-task">{{ task }}</span>
    <span class="task-card-stat">{{ status }}</span>
    <div class="delete-task-button">
      <img class="delete-task-button-img"
           src="@/assets/Close.svg"
           alt="del-task"
           @click="">
    </div>
  </div>
</template>

<script>
export default {
  props: ['pk', 'employee', 'task', 'status'],
  methods: {

  }
}
</script>

<style scoped>
.task-card {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
}

.delete-task-button {
  width: 23px;
  //border: 1px solid red;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.delete-task-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.delete-task-button-img {
  width: 100%;
}

.task-card-empl {
  width: 30%
}

.task-card-task {
  width: 44%
}

.task-card-stat {
  width: 21%
}
</style>