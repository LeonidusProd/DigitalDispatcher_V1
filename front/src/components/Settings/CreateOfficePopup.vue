<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление УК</h3>
          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="closeDialog">
          </div>
        </div>
        <div class="down-block">
          <h5>Название УК</h5>
          <MyInput :placeholder="'Название УК'"
                   :model-value="this.officeName"
                   @input="this.officeName = $event.target.value">
          </MyInput>
          <h5>Адрес УК</h5>
          <MySelect :options="this.addresses"
                    @selectChanged="addressChanged">
          </MySelect>
          <h5>График работы</h5>
          <MySelect :options="this.workSchedules"
                    @selectChanged="workScheduleChanged">
          </MySelect>
          <MyButton @click="saveOffice">
            Сохранить
          </MyButton>
          <!--          <h5>Задача:</h5>-->
          <!--          <MySelect :options="this.standartServices"-->
          <!--                    @selectChanged="serviceChanged"></MySelect>-->
          <!--          <h5 v-if="showEmploeesSelect">Сотрудник:</h5>-->
          <!--          <MySelect v-if="showEmploeesSelect"-->
          <!--                    :options="this.serviceEmployees"-->
          <!--                    @selectChanged="employeeChanged">-->
          <!--          </MySelect>-->

          <!--          <my-button v-if="showSaveButton"-->
          <!--                     @click="saveTask">-->
          <!--            Сохранить-->
          <!--          </my-button>-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MySelect from "@/components/UI/MySelect.vue";
import {mapActions, mapMutations} from "vuex";
import MyInput from "@/components/UI/MyInput.vue";
import axios from "axios";

export default {
  components: {MyButton, MySelect, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      officeName: '',
      selectedAddress: -1,
      addresses: [],
      selectedworkSchedule: -1,
      workSchedules: [],
    }
  },
  mounted() {
    this.loadAddresses()
    this.loadWorkSchedules()
  },
  methods: {
    async loadAddresses() {
      try {
        const response = (await axios.get('http://localhost:8000/api/v1/address/'))
        this.addresses = response.data
      } catch (e) {
        alert('Сервер не доступен')
      }
    },
    async loadWorkSchedules() {
      try {
        const response = (await axios.get('http://localhost:8000/api/v1/schedule/'))
        this.workSchedules = response.data
      } catch (e) {
        alert('Сервер не доступен')
      }
    },
    addressChanged(addressPk) {
      this.selectedAddress = addressPk
    },
    workScheduleChanged(workSchedulePk) {
      this.selectedworkSchedule = workSchedulePk
    },
    closeDialog() {
      this.$emit('closeDialog')
    },
    saveOffice() {
      if (this.officeName !== '' && this.selectedAddress !== -1 && this.selectedworkSchedule !== -1) {
        // this.createOffice()
        this.$emit('saveOffice', {
          name: this.officeName,
          address: this.selectedAddress,
          work_schedule: this.selectedworkSchedule
        })
        this.officeName = ''
        this.servicePk = -1
        this.employeePk = -1
        this.$emit('closeDialog')
      }
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
  min-height: 320px;
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
</style>