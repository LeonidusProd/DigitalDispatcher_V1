<template>
<h4>{{ requestListLanding }}</h4>
  <h6 v-if="requests.length === 0">Нет заявок</h6>
  <div v-else class="requests-list-scroll custom-scroll" id="requests-list">
    <ShortRequestCard v-for="request in requests"
                      :request="request"
                      @click=this.setActiveRequestId(request.pk)
                      :class="{'active-button': this.activeRequestId === request.pk}">
    </ShortRequestCard>
  </div>
</template>

<script>
import {mapMutations, mapState} from "vuex";
import ShortRequestCard from "@/components/RequestManage/ShortRequestCard.vue";

export default {
  props: {
    requestListLanding: [String],
    requests: [Array]
  },
  components: {ShortRequestCard},
  computed: {
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
    }),
  },
  methods: {
    ...mapMutations({
      setActiveRequestId: "requests/setActiveRequestId"
    }),
  },
}
</script>

<style scoped>
.requests-list-scroll {
  height: 95%;
  overflow-y: auto;
  padding-right: 3px;
  border-radius: 12px;
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
.active-button {
  background-color: rgb(79, 212, 213);
}
.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>