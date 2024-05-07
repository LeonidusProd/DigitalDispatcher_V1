<template>
  <div class="dialog" v-if="show">
    <div class="dialog-content">
      <div class="create-task-content">
        <div class="up-block">
          <h3>Добавление графика работы</h3>

          <div class="close-dialog-button">
            <img class="close-dialog-button-img"
                 src="@/assets/Close.svg"
                 alt="close-dialog"
                 @click="closeDialog">
          </div>
        </div>

        <div class="down-block">
          <h5>Название графика работы</h5>
          <MyInput :placeholder="'Название графика работы'"
                   :model-value="this.scheduleName"
                   @input="this.scheduleName = $event.target.value">
          </MyInput>

          <h5>Расписание</h5>
          <MyCheckbox :checked="this.mondayIsWork"
                      @update:checked="mondayIsWork = $event"
                      :label="'Понедельник рабочий'">
          </MyCheckbox>

          <MyButton @click="saveSchedule">
            Сохранить
          </MyButton>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton.vue";
import MySelect from "@/components/UI/MySelect.vue";
import MyInput from "@/components/UI/MyInput.vue";
import axios from "axios";
import MyCheckbox from "@/components/UI/MyCheckBox.vue";

export default {
  components: {MyCheckbox, MyButton, MySelect, MyInput},
  props: {
    show: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      scheduleName: '',
      mondayIsWork: false,
      // selectedAddress: -1,
      // addresses: [],
      // selectedworkSchedule: -1,
      // workSchedules: [],
    }
  },
  mounted() {
    // this.loadAddresses()
    // this.loadWorkSchedules()
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
      this.$emit('closeScheduleDialog')
    },
    saveSchedule() {
      // if (this.officeName !== '' && this.selectedAddress !== -1 && this.selectedworkSchedule !== -1) {
      //   this.$emit('saveSchedule', {
      //     name: this.officeName,
      //     address: this.selectedAddress,
      //     work_schedule: this.selectedworkSchedule
      //   })
      //   this.officeName = ''
      //   this.servicePk = -1
      //   this.employeePk = -1
      // }
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
  min-width: 600px;
  padding: 20px;
  display: flex;
}

.create-task-content {
  width: 100%;
  background: rgb(169, 168, 159, 0.2);
  border-radius: 10px;
  padding: 10px;
}

.up-block {
  height: 30px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
}

.down-block {
  height: 90%;
  width: 100%;
  padding: 20px;
}

.close-dialog-button {
  height: 30px;
  width: 30px;
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