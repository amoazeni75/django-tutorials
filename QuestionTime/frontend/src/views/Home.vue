<template>
    <div class="home">
        <div class="container">
            <div v-for="question in questions"
                 :key="question.pk">
                <p class="mb-0">Posted by:
                    <span class="question-author">{{question.author}} </span>
                </p>
                <h2>
                    <router-link
                            :to="{name :'Question', params : {slug:question.slug}}"
                            class="question-link"
                    >
                        {{question.content}}
                    </router-link>
                </h2>
                <p>Answers: {{question.answers_count}}</p>
                <hr>
            </div>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import {apiService} from "../common/api.service";

    export default {
        name: "Home",
        data() {
            return {
                questions: []
            }
        },
        methods: {
            getQuestions() {
                let endpoint = "/api/questions/"
                apiService(endpoint)
                    .then(data => {
                        this.questions.push(...data.results);
                    })
            }
        },
        created() {
            this.getQuestions();
            document.title = "QuestionTime"
        }
    };
</script>
<style scoped>
    .question-author {
        font-weight: bold;
        color: #DC3545;
    }

    .question-link {
        font-weight: bold;
        color: black;
    }

    .question-link:hover {
        text-decoration: none;
        color: #343A40;
    }
</style>