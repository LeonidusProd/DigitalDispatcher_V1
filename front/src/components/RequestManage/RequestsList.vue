<template>
  <h4>{{ requestListLanding }}</h4>
  <h6 v-if="requests.length === 0">Нет заявок</h6>
  <div v-else class="requests-list-scroll custom-scroll" id="requests-list">
    <ShortRequestCard v-for="request in requests"
                      :id=request.pk
                      :date=request.date
                      :address=request.address
                      :info=request.info
                      @click=makeActive(request.pk)
                      :class="{'active-button': this.activeRequestId === request.pk}">
    </ShortRequestCard>

    <!--    <ShortRequestCard date="Заявка от 23.04.2024 в 16:00"-->
    <!--                      adress="Ул. Пупина, д. 13"-->
    <!--                      info="Нет света"-->
    <!--                      class="">-->
    <!--    </ShortRequestCard>-->
  </div>
</template>

<script>
import ShortRequestCard from "@/components/RequestManage/ShortRequestCard.vue";
import store from "@/store";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";

export default {
  computed: {
    store() {
      return store
    },
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      activeSection: state => state.requests.activeSection,
    }),
    ...mapGetters({})
  },
  components: {ShortRequestCard},
  props: ['requests', 'requestListLanding'],
  methods: {
    ...mapMutations({
      setActiveSection: "requests/setActiveSection",
      setActiveRequestId: "requests/setActiveRequestId"
    }),
    ...mapActions({
      loadRequestData: 'requests/loadRequestData'
    }),
    makeActive(pk) {
      this.setActiveRequestId(pk)
    },
  }
}
</script>

<style scoped>
.requests-list-scroll {
  height: 95%;
  overflow-y: auto;
  padding-right: 3px;
  border-radius: 12px;
  //border: 1px solid black;
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

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>