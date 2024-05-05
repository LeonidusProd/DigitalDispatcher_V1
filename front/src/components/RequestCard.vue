<template>
  <h4>Информация о заявке № {{ this.activeRequestId }}</h4>
  <div class="request-card-content">
    <div class="request-card-up">
      <div class="request-card-info-block custom-scroll">
              <span>
                <b>Сообщение жителя:</b><br>
                {{ this.requestData['info'] }}
              </span>
        <span>
          <b>Дата:</b> {{ this.requestData['date'].split(' ')[0] }} в {{ this.requestData['date'].split(' ')[1] }}
        </span>
        <span><b>Статус:</b> {{ this.requestData['status'] }}</span>
        <span><b>Житель:</b> {{ this.requestData['resident'] }}</span>
        <span><b>Адрес:</b> {{ this.requestData['address'] }}</span>
      </div>
      <div class="request-card-photo-block">
        <b>Прикреплённая фотография:</b><br>
        <h6 v-if="this.requestData['photo'] === null">Житель не прикрепил фотографию</h6>
        <div v-else class="request-photo">
          <img :src="this.requestData['photo']" alt="problem-photo">
        </div>

      </div>
    </div>
    <div class="request-card-tasks-block" id="request_card_tasks_block">
      <h4>Назначенные задачи</h4>
      <RequestTasksList :key="taskListKey"
                        @deleteTask="reloadTasks()">
      </RequestTasksList>
      <div class="create-task-button" @click="this.showDialog = true">Создать задачу</div>
      <CreateTaskPopup
          :show="this.showDialog"
          @closeDialog="this.showDialog = false"
          @saveTask="saveTask"
      ></CreateTaskPopup>
    </div>
  </div>
</template>

<script>
import store from "@/store";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import RequestsList from "@/components/RequestsList.vue";
import ShortRequestCard from "@/components/ShortRequestCard.vue";
import MyButton from "@/components/UI/MyButton.vue";
import RequestTasksList from "@/components/RequestTasksList.vue";
import {getCurrentInstance} from "vue";
import CreateTaskPopup from "@/components/CreateTaskPopup.vue";

export default {
  computed: {
    store() {
      return store
    },
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      requestTasks: state => state.requests.requestTasks,
      requestData: state => state.requests.requestData,
      requests: state => state.requests.requests,
      taskListKey: state => state.requests.taskListKey,
    }),
    ...mapGetters({})
  },
  components: {CreateTaskPopup, RequestTasksList},
  data() {
    return {
      showDialog: false
    }
  },
  created() {
    this.loadRequestTasks(this.activeRequestId);
    this.loadRequestData(this.activeRequestId)
  },
  methods: {
    ...mapMutations({
      setTaskListKey: "requests/setTaskListKey",
    }),
    ...mapActions({
      loadRequestTasks: 'requests/loadRequestTasks',
      loadRequestData: 'requests/loadRequestData',
      createTask: 'requests/createTask',
    }),
    reloadTasks() {
      // console.log(this.taskListKey);
      // this.taskListKey += 1;
      // console.log(this.taskListKey);
      this.loadRequestTasks(this.activeRequestId);
      this.setTaskListKey(this.taskListKey + 1)
      // getCurrentInstance().proxy.$forceUpdate();

    },
    saveTask(servicePk, employeePk) {
      this.createTask({
        requestPk: this.activeRequestId,
        servicePk: servicePk,
        employeePk: employeePk,
        status: 1
      })
      this.reloadTasks()
      this.showDialog = false
    },
  }
}
</script>

<style scoped>
.request-card-content {
  //border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 94%;
}

.request-card-up {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 49%;
  //border: 1px solid red;
  //padding: 10px;
}

.request-card-info-block {
  width: 49%;
  display: flex;
  flex-direction: column;
  //border: 1px solid yellow;
  overflow-y: auto;
}

.request-card-photo-block {
  width: 49%;
  //border: 1px solid pink;
}

.request-photo {
  width: 95%;
  height: 95%;
  display: flex;
  vertical-align: middle;
  border-radius: 11px;
  overflow: hidden;
}

.request-photo img {
  width: 100%;
  height: 100%;
  border-radius: 11px;
  object-fit: cover;
}

.request-card-tasks-block {
  //border: 1px solid blue;
  height: 49%;
}

.create-task-button {
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  padding-left: 20px;
  align-items: center;
  width: 200px;
}

.create-task-button:hover {
  display: flex;
  background-color: rgb(109, 197, 195, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  padding-left: 20px;
  align-items: center;
  cursor: default;
  width: 200px;
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