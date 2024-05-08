<template>
  <h5 v-if="false">Список типовых задач пуст</h5>

  <div v-else class="service-cards">
    <div class="service-list custom-scroll">
      <ServiceCard v-for="service in this.servicesList"
                  :pk="service.pk"
                  :service-name="service.name"
                  @deleteService="$emit('deleteService')">
      </ServiceCard>
    </div>
  </div>
</template>

<script>
import ServiceCard from "@/components/Settings/ServiceCard.vue";

export default {
  components: {ServiceCard},
  props:{
    servicesList: [Array]
  }
}
</script>

<style scoped>
.service-cards {
  height: 150px;
}
.service-list {
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