<template>
  <h5 v-if="false">Список УК пуст</h5>
  <div v-else class="office-cards">
    <div class="office-list custom-scroll">
      <OfficeCard v-for="office in this.officesList"
                  :pk="office.pk"
                  :office-name="office.name"
                  @deleteOffice="$emit('deleteOffice')">
      </OfficeCard>
    </div>
  </div>
</template>

<script>
import RequestTaskCard from "@/components/RequestManage/RequestTaskCard.vue";
import OfficeCard from "@/components/Settings/OfficeCard.vue";
import axios from "axios";
import MyButton from "@/components/UI/MyButton.vue";

export default {
  components: {MyButton, OfficeCard, RequestTaskCard},
  props:{
    officesList: [Array]
  }
}
</script>

<style scoped>
.office-cards {
  //display: flex;
  //flex-direction: column;
  height: 150px;
  border: 1px solid purple;
}

.office-list {
  //border: 1px solid blue;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding-right: 3px;
  margin-top: 3px;
  border-radius: 12px;
  height: 140px;
  //min-height: 65%;
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

.task-card-headers {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  width: 99%;
  height: 32px;
  //height: 15%;
  //min-height: 15%;
  display: flex;
  background-color: rgb(109, 197, 195, 0.4);
}

.custom-scroll::-webkit-scrollbar {
  width: 5px; /* Ширина полосы прокрутки */
}

/* Фон полосы прокрутки */
.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
  border-radius: 6px;
}

/* Стиль ползунка */
.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}

/* Цвет ползунка при наведении */
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>