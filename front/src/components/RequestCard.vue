<template>
  <h4>Информация о заявке № {{ activeRequestId }}</h4>
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
        <span><b>Статус:</b> {{ requestData['status'] }}</span>
        <span><b>Житель:</b> {{ requestData['resident'] }}</span>
        <span><b>Адрес:</b> {{ requestData['adress'] }}</span>
      </div>
      <div class="request-card-photo-block">
        <b>Прикреплённая фотография:</b><br>
        <h6 hidden="">Житель не прикрепил фотографию</h6>
        <div class="request-photo">
          <img src="@/assets/hige.jpg" alt="problem-photo">
        </div>

      </div>
    </div>
    <div class="request-card-tasks-block">
      <h4>Назначенные задачи</h4>
      <h5 hidden="hidden">Нет назначенных задач</h5>
      <div class="task-card-headers">
        <span class="task-card-empl">Сотрудник</span>
        <span class="task-card-task">Услуга</span>
        <span class="task-card-stat">Статус</span>
      </div>
      <div class="tasks-list custom-scroll">
        <div class="task-card">
          <span class="task-card-empl">Сотрудник</span>
          <span class="task-card-task">Услуга</span>
          <span class="task-card-stat">Статус</span>
          <div class="delete-task-button">
            <img class="delete-task-button-img" src="@/assets/Close.svg" alt="del-task">
          </div>
        </div>
        <div class="task-card">
          <span class="task-card-empl">Сотрудник</span>
          <span class="task-card-task">Услуга</span>
          <span class="task-card-stat">Статус</span>
          <div class="delete-task-button">
            <img class="delete-task-button-img" src="@/assets/Close.svg" alt="del-task">
          </div>
        </div>
        <div class="task-card">
          <span class="task-card-empl">Сотрудник</span>
          <span class="task-card-task">Услуга</span>
          <span class="task-card-stat">Статус</span>
          <div class="delete-task-button">
            <img class="delete-task-button-img" src="@/assets/Close.svg" alt="del-task">
          </div>
        </div>
        <div class="task-card">
          <span class="task-card-empl">Сотрудник</span>
          <span class="task-card-task">Услуга</span>
          <span class="task-card-stat">Статус</span>
          <div class="delete-task-button">
            <img class="delete-task-button-img" src="@/assets/Close.svg" alt="del-task">
          </div>
        </div>
        <div class="task-card">
          <span class="task-card-empl">Сотрудник</span>
          <span class="task-card-task">Услуга</span>
          <span class="task-card-stat">Статус</span>
          <div class="delete-task-button">
            <img class="delete-task-button-img" src="@/assets/Close.svg" alt="del-task">
          </div>
        </div>
      </div>
      <div class="create-task-button">Создать задачу</div>
    </div>
  </div>
</template>

<script>
import store from "@/store";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import RequestsList from "@/components/RequestsList.vue";
import ShortRequestCard from "@/components/ShortRequestCard.vue";
import MyButton from "@/components/UI/MyButton.vue";

export default {
  // props: ['requestId'],
  computed: {
    store() {
      return store
    },
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      requestTasks: state => state.requests.requestTasks,
      requestData: state => state.requests.requestData,
      requests: state => state.requests.requests,
    }),
    ...mapGetters({})
  },
  components: {},
  data() {
    return {}
  },
  created() {
    this.loadRequestTasks(this.requestId);
    this.loadRequestData(this.requestId)
  },
  methods: {
    ...mapMutations({}),
    ...mapActions({
      loadRequestTasks: 'requests/loadRequestTasks',
      loadRequestData: 'requests/loadRequestData'
    }),
    changeSection(section) {

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

.request-card-tasks-block {
  //border: 1px solid blue;
  height: 49%;
}

.tasks-list {
  //border: 1px solid blue;
  display: flex;
  flex-direction: column;
  height: 55%;
  overflow-y: auto;
  padding-right: 3px;
  margin-top: 3px;
  border-radius: 12px;
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

.task-card {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  display: flex;
  background-color: rgb(139, 182, 177, 0.4);
}

.delete-task-button {
  width: 23px;
  //border: 1px solid red;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.delete-task-button:hover {
  width: 23px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.delete-task-button-img {
  width: 100%;
}

.task-card-headers {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  width: 99%;
  display: flex;
  background-color: rgb(109, 197, 195, 0.4);
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