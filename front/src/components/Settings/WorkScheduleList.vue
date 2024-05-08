<template>
  <h5 v-if="false">Список графиков пуст</h5>

  <div v-else class="schedule-cards">
    <div class="schedule-list custom-scroll">
      <WorkScheduleCard v-for="schedule in this.schedulesList"
                  :pk="schedule.pk"
                  :schedule-name="schedule.name"
                  @deleteSchedule="$emit('deleteSchedule')">
      </WorkScheduleCard>
    </div>
  </div>
</template>

<script>
import WorkScheduleCard from "@/components/Settings/WorkScheduleCard.vue";

export default {
  components: {WorkScheduleCard},
  props:{
    schedulesList: [Array]
  }
}
</script>

<style scoped>
.schedule-cards {
  height: 150px;
}
.schedule-list {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding-right: 3px;
  margin-top: 3px;
  border-radius: 12px;
  height: 170px;
}
.custom-scroll::-webkit-scrollbar {
  width: 5px;
}
.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
  border-radius: 6px;
}
.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}
.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>