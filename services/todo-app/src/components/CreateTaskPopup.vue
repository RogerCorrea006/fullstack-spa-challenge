<template>
  <v-row justify="end">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn large dark color="purple" v-bind="attrs" v-on="on">
          Adicionar nova tarefa
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Nova Tarefa</span>
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
          <v-btn color="blue darken-1" text @click="dialog = false">
            Fechar
          </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Salvar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "../plugins/axios";
import {Task} from "../interfaces/task"

@Component
export default class CreateTaskPopup extends Vue {
  dialog = false;
  task: Task = {
    name: "",
    description: "",
  };
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
        "/task/createTask",
        {
          name: this.task.name,
          description: this.task.description,
        }
      );
      console.log(response.data)

      this.dialog = false;

      this.task.name = ""
      this.task.description = ""

      this.$emit('taskCreated')

    } catch (error) {
      console.error("erro ao criar a tarefa:", error);
    }
  }
}
</script>