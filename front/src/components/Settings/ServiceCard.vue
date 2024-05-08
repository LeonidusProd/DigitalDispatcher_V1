<template>
  <div class="service-card">
    <span>{{ this.serviceName }}</span>

    <div class="delete-service-button">
      <img class="delete-service-button-img"
           src="@/assets/Close.svg"
           alt="del-sevice"
           @click="deleteService(this.pk)">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ['pk', 'serviceName'],
  methods: {
    async deleteService(pk) {
      await axios.delete(`http://localhost:8000/api/v1/service/delete/${pk}`)
      this.$emit('deleteService')
    }
  }
}
</script>

<style scoped>
.service-card {
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
  justify-content: space-between;
}
.delete-service-button {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}
.delete-service-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}
.delete-service-button-img {
  width: 100%;
}
</style>