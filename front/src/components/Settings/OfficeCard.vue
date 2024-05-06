<template>
<div class="office-card">
    <span class="office-card-name">{{ this.officeName }}</span>
    <div class="delete-office-button">
      <img class="delete-office-button-img"
           src="@/assets/Close.svg"
           alt="del-office"
           @click="deleteOffice(this.pk)">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ['pk', 'officeName'],
  methods: {
    async deleteOffice(pk) {
      await axios.delete(`http://localhost:8000/api/v1/office/delete/${pk}`)
      this.$emit('deleteOffice')
    }
  }
}
</script>

<style scoped>
.office-card {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
  justify-content: space-between;
}

.delete-office-button {
  width: 23px;
  //border: 1px solid red;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.delete-office-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.delete-office-button-img {
  width: 100%;
}

.office-card-name {
  //width: 30%
}
</style>