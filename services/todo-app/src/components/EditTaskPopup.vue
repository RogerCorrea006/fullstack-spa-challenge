<template>
  
   
      <v-card>
        <v-card-title>
          <span class="text-h5">Editar Tarefa</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="task.name"
                  label="Título"
                  required
                  counter
                  maxlength="20"
                  :rules="rules"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  v-model="task.description"
                  name="input-7-4"
                  label="Descrição"
                  value=""
                  counter
                  maxlength="100"
                  required
                  :rules="rules"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="$emit('closeDialog')">
            Fechar
          </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Salvar </v-btn>
        </v-card-actions>
      </v-card>
   

</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "../plugins/axios";
import { PropType } from "vue/types/v3-component-props";
import {Task} from "../interfaces/task"

const CardTask = Vue.extend({
  props: {
    editTask: { type: Object as PropType<Task> },
  },
});

@Component
export default class EditTaskPopup extends CardTask {
  task:Task = {id: this.editTask.id, name:this.editTask.name, description: this.editTask.description}
  rules = [
    (value: string) => !!value || "Campo obrigatório",
  ]
  

  data() {
    return {};
  }

  async save() {
    
    if(this.task.name == "" || this.task.description == "") return

    try {
      const response = await axios.post(
        "/task/updateTask",
        {
          id: this.task.id,
          name: this.task.name,
          description: this.task.description,
        }
      );
      console.log(response.data);

      this.$emit('closeDialog')
      this.$emit('tasksUpdated')

    } catch (error) {
      console.error("erro ao editar a tarefa:", error);
    }
  }

}
</script>