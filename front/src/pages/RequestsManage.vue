<template>
  <div class="container">
    <div class="left-side-menu">
      <div class="up-block">
        <div class="logo-block">
          <img class="logo-img" src="@/assets/Лого%20текст%20снизу.svg" alt="logo">
        </div>
        <div class="menu-block">
          <my-button @click="changeSection('newRequests')"
                     :class="{'active-button':this.activeSection === 'newRequests'}">
            Новые заявки
          </my-button>
          <my-button @click="changeSection('activeRequests')"
                     :class="{'active-button':this.activeSection === 'activeRequests'}">
            Активные заявки
          </my-button>
        </div>
      </div>
      <div class="down-block">
        <my-button @click="">
          Выход
        </my-button>
      </div>
    </div>

    <div class="workspace">
      <div class="requests-list">
        <requests-list
            :requests=this.requests
            :request-list-landing="requestListLanding">
        </requests-list>
      </div>

      <div class="request-card">
        <h4 v-if="this.activeRequestId === -1">Ни одна заявка не выбрана</h4>
        <RequestCard v-else :key="this.activeRequestId">
        </RequestCard>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import ShortRequestCard from "@/components/RequestManage/ShortRequestCard.vue";
import RequestsList from "@/components/RequestManage/RequestsList.vue";
import store from "@/store";
import {mapState, mapMutations, mapActions, mapGetters} from 'vuex'
import RequestCard from "@/components/RequestManage/RequestCard.vue";

export default {
  computed: {
    store() {
      return store
    },
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      activeSection: state => state.requests.activeSection,
      requests: state => state.requests.requests,
      taskListKey: state => state.requests.taskListKey,
    }),
    ...mapGetters({})
  },
  components: {RequestCard, RequestsList, ShortRequestCard, MyButton},
  data() {
    return {
      requestListLanding: ''
    }
  },
  mounted() {
    this.requestListLanding = 'Новые заявки'
    this.loadNewRequests();
  },
  methods: {
    ...mapMutations({
      setActiveSection: "requests/setActiveSection",
      setActiveRequestId: "requests/setActiveRequestId"
    }),
    ...mapActions({
      loadNewRequests: 'requests/loadNewRequests',
      loadActiveRequests: "requests/loadActiveRequests"
    }),
    changeSection(section) {
      this.setActiveSection(section)
      if (section === 'newRequests') {
        this.loadNewRequests()
        this.requestListLanding = 'Новые заявки'
      } else if (section === 'activeRequests') {
        this.requestListLanding = 'Активные заявки'
        this.loadActiveRequests()
      }
      this.setActiveRequestId(-1)
    },
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  min-height: 400px;
  height: 94vh;
}

.left-side-menu {
  background-color: rgb(169, 168, 159, 0.2);
  width: 20%;
  padding: 10px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.logo-block {
  text-align: center;
}

.logo-img {
  width: 50%;
}

.down-block {
  width: 100%;
}

.workspace {
  background-color: rgb(169, 168, 159, 0.2);
  width: 79%;
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-radius: 20px;
}

.requests-list {
  width: 35%;
  border: 1px;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px 10px 15px;
}

.request-card {
  width: 64%;
  //border: 1px solid #212523;
  background-color: rgb(169, 168, 159, 0.4);
  border-radius: 12px;
  padding: 10px;

}

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>