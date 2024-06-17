<template>
  <v-container class="my-5">
    <v-row justify="end">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <edit-task-popup v-if="editDialog" :editTask="dialogTask" v-on:closeDialog="closeDialog(true)" v-on:tasksUpdated="onTasksUpdated" />
            <delete-task-popup v-else-if="deleteDialog" :editTask="dialogTask" v-on:closeDialog="closeDialog(false)" v-on:tasksUpdated="onTasksUpdated" />
        </v-dialog>
    </v-row>
    
    <v-row v-for="task in tasks" :key="task.id">
      <v-col>
        <v-card color="#CE9DD9" dark>
          <v-card-title>
            <span class="text-h6 font-weight-light">{{task.name}}</span>
          </v-card-title>

          <v-card-text class="text-h5 font-weight-bold">
            
            <span class="text-card"> {{task.description}}</span>
            
          </v-card-text>

          <v-card-actions>
            <v-list-item class="grow">
              <v-row align="center" justify="start">
                <v-btn icon @click="openDialog(task, true)"><v-icon class="mr-1"> mdi-pencil </v-icon></v-btn>
                <v-btn icon @click="openDialog(task, false)"><v-icon class="mr-1" color="red"> mdi-delete </v-icon></v-btn>                
              </v-row>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
.text-card{
  color: white;
}
</style>


<script lang="ts">


import Vue from "vue";
import Component from "vue-class-component";
import { PropType } from "vue/types/v3-component-props";
import DeleteTaskPopup from "./DeleteTaskPopup.vue";
import EditTaskPopup from "./EditTaskPopup.vue" 
import {Task} from "../interfaces/task"

const HomePage = Vue.extend({
  props: {
    tasks: { type: [] as PropType<Task> },
  },
});

@Component({
    components: {EditTaskPopup, DeleteTaskPopup},
})
export default class CardTask extends HomePage {

    dialog = false
    editDialog = false
    deleteDialog = false 
    dialogTask: Task = { id: 0, name: "", description: ""}

    openDialog(task: Task, editDialog: boolean){

        this.dialogTask = task

        if(editDialog){
            this.editDialog = true
        } else {
            this.deleteDialog = true
        }

        this.dialog = true

        console.log(this.dialogTask.name)

    }

    async closeDialog(editDialog: boolean){
        
         if(editDialog){
            this.editDialog = false
        } else {
            this.deleteDialog = false
        }
        
        this.dialog = false

    }

    async onTasksUpdated(){
        this.$emit('getTasks')
    }

}
</script>