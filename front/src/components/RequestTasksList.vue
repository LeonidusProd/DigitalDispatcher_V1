<template>
  <h5 v-if="requestTasks.length === 0">Нет назначенных задач</h5>
  <div v-else>
    <div class="task-card-headers">
    <span class="task-card-empl">Сотрудник</span>
    <span class="task-card-task">Задача</span>
    <span class="task-card-stat">Статус</span>
  </div>
  <div class="tasks-list custom-scroll">
    <RequestTaskCard v-for="task in this.requestTasks"
                     :pk="task.pk"
                     :employee="task.employee"
                     :task="task.task"
                     :status="task.status"
                     @deleteTask="$emit('deleteTask')">
    </RequestTaskCard>
  </div>
  </div>
</template>

<script>
import store from "@/store";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import RequestsList from "@/components/RequestsList.vue";
import ShortRequestCard from "@/components/ShortRequestCard.vue";
import MyButton from "@/components/UI/MyButton.vue";
import RequestTaskCard from "@/components/RequestTaskCard.vue";
import { getCurrentInstance } from 'vue';

export default {
  // props: ['pk'],
  computed: {
    store() {
      return store
    },
    ...mapState({
      activeRequestId: state => state.requests.activeRequestId,
      requestTasks: state => state.requests.requestTasks,
      taskListKey: state => state.requests.taskListKey,
      // requestData: state => state.requests.requestData,
      // requests: state => state.requests.requests,
    }),
    ...mapGetters({})
  },
  components: {RequestTaskCard},
  data() {
    return {}
  },
  created() {
    this.loadRequestTasks(this.activeRequestId);
    // this.loadRequestData(this.requestId)
  },
  methods: {
    ...mapMutations({
      setTaskListKey: "requests/setTaskListKey",
    }),
    ...mapActions({
      loadRequestTasks: 'requests/loadRequestTasks',
      // loadRequestData: 'requests/loadRequestData'
    }),
    reRender() {
      console.log('reRender')
      // this.$emit('deleteTask')
      this.setTaskListKey(this.taskListKey + 1)
    },
  }
}
</script>

<style scoped>
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

.task-card-headers {
  //border: 1px solid red;
  border-radius: 10px;
  margin-top: 7px;
  padding: 3px 10px;
  width: 99%;
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