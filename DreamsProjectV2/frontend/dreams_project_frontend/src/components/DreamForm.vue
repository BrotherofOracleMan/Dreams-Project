<template>
    <div>
        <form @submit.prevent="submitForm">
            <div>
                <label for="dreamname">Dream Name:</label>
                <input type = "text" id="dreamname" v-model="formData.dreamName" required>
            </div>
            <div>
                <label for="selectedDate"> </label>
                <input type="date" id="selectedDate" v-model="formData.selectedDate" required>
            </div>
            <div>
                <label for="dreamdescription">Dream Description</label>
                <textarea id="DreamDescription" v-model="formData.dreamDescription" required></textarea>
            </div>
        </form>
        <button type="submit">submit</button>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                formData:{
                    dreamName:'',
                    selectedDate:'',
                    dreamDescription:'',
                },
                formSubmitted: false
            }
        },
        methods:{
            submitForm(){
                this.formSubmitted= true
            }
        }
    }
</script>

<style scoped>

</style>