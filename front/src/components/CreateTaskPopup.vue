<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Создание задачи</h3>
          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="closeDialog">
          </div>
        </div>
        <div class="down-block">
          <h5>Задача:</h5>
          <MySelect :options="this.standartServices"
                    @selectChanged="serviceChanged"></MySelect>
          <h5 v-if="showEmploeesSelect">Сотрудник:</h5>
          <MySelect v-if="showEmploeesSelect"
                    :options="this.serviceEmployees"
                    @selectChanged="employeeChanged"></MySelect>
          <div v-if="showSaveButton"
               @click="$emit('saveTask', this.servicePk, this.employeePk)"
               class="save-button">
            Сохранить
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import MySelect from "@/components/UI/MySelect.vue";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import store from "@/store";

export default {
  computed: {
    store() {
      return store
    },
    ...mapState({
      // activeRequestId: state => state.requests.activeRequestId,
      standartServices: state => state.requests.standartServices,
      serviceEmployees: state => state.requests.serviceEmployees,
      requestData: state => state.requests.requestData,
    }),
    ...mapGetters({})
  },
  components: {MySelect},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      servicePk: -1,
      showEmploeesSelect: false,
      showSaveButton: false,
      employeePk: -1,
    }
  },
  mounted() {
    this.loadStandartServices()
  },
  methods: {
    ...mapMutations({
      // setActiveSection: "requests/setActiveSection",
    }),
    ...mapActions({
      // loadNewRequests: 'requests/loadNewRequests',
      loadStandartServices: 'requests/loadStandartServices',
      loadServiceEmployees: 'requests/loadServiceEmployees',
    }),
    closeDialog() {
      this.$emit('closeDialog')
    },
    serviceChanged(ServicePk) {
      // console.log('this.requestData[\'office_id\']: ' + this.requestData.office_id)
      this.servicePk = ServicePk
      this.loadServiceEmployees({
        position_pk: ServicePk,
        office_pk: this.requestData['office_id']
      })
      this.showEmploeesSelect = true
      // console.log('this.serviceEmployees ' + this.serviceEmployees)
    },
    employeeChanged(EmployeePk) {
      this.employeePk = EmployeePk
      console.log('ServicePk: ' + this.servicePk)
      console.log('EmployeePk: ' + this.employeePk)
      this.showSaveButton = true
    },

  }
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background: rgb(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}

.dialog-content {
  margin: auto;
  background: white;
  border-radius: 12px;
  height: 320px;
  width: 400px;
  padding: 20px;
  display: flex;
}

.create-task-content {
  width: 100%;
  background: rgb(169, 168, 159, 0.2);
  border-radius: 10px;
  padding: 10px;
  //border: 1px solid black;
}

.up-block {
  height: 30px;
  width: 100%;
  //border: 1px solid red;
  display: flex;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
}

.down-block {
  height: 90%;
  width: 100%;
  //border: 1px solid blue;
  padding: 20px;
}

.close-dialog-button {
  height: 30px;
  width: 30px;
  //border: 1px solid red;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.4);
  border-radius: 11px;
}

.close-dialog-button:hover {
  height: 30px;
  width: 30px;
  display: flex;
  vertical-align: middle;
  background-color: rgb(109, 197, 195, 0.9);
  border-radius: 11px;
}

.close-dialog-button-img {
  width: 100%;
}

.save-button {
  display: flex;
  flex-direction: column;
  width: 150px;
  background-color: rgb(139, 182, 177, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  justify-content: space-evenly;
  text-align: center;
}

.save-button:hover {
  display: flex;
  flex-direction: column;
  width: 150px;
  background-color: rgb(109, 197, 195, 0.4);
  margin-top: 10px;
  height: 40px;
  border-radius: 20px;
  justify-content: space-evenly;
  text-align: center;
  cursor: default;
}
</style>