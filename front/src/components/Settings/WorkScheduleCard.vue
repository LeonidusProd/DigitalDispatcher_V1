<template>
  <div class="schedule-card">
    <span>{{ this.scheduleName }}</span>

    <div class="delete-schedule-button">
      <img class="delete-schedule-button-img"
           src="@/assets/Close.svg"
           alt="del-office"
           @click="deleteSchedule(this.pk)">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ['pk', 'scheduleName'],
  methods: {
    async deleteSchedule(pk) {
      await axios.delete(`http://localhost:8000/api/v1/schedule/delete/${pk}`)
      this.$emit('deleteSchedule')
    }
  }
}
</script>

<style scoped>
.schedule-card {
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
  justify-content: space-between;
}
.delete-schedule-button {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}
.delete-schedule-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}
.delete-schedule-button-img {
  width: 100%;
}
</style>