<template>
  <v-container class="my-5">
    <create-task-popup v-on:taskCreated="onTaskCreated"/>

    <edit-task :tasks="tasks" v-on:taskDelete="onTaskDelete"/>
  </v-container>
</template>

<script lang="ts">
import axios from "../plugins/axios";
import Vue from "vue";
import Component from "vue-class-component";
import CreateTaskPopup from "./CreateTaskPopup.vue";
import EditTask from "./EditTask.vue";
import {Task} from "../interfaces/task"

@Component({
  components: {
    CreateTaskPopup,
    EditTask
  },
})
export default class TasksPage extends Vue {

  tasks: Task[] = []

  mounted(){
    this.getTasks()
  }

  async getTasks() {

    try {

      const response = await axios.get<Task[]>('/task/getTasks')
      let tasksData = response.data

      this.tasks = tasksData.map((task) => {
        task.editable = false
        return task
      })

    } catch (error){
      console.error('erro ao buscas as tarefas:', error)
    }

    
  }

  async onTaskDelete(){

    await this.getTasks()
  }

   async onTaskCreated(){

    await this.getTasks()
  }

  data() {
    return {};
  }
}
</script>