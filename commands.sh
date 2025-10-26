# !/bin/bash

activate_back() {
    source $(pwd)/app/back/.venv/bin/activate
}

db_apply() {
    PYTHONPATH=$PYTHONPATH alembic upgrade head
}

dev_commands(){
    PYTHONPATH=/home/gabriel/personal/herokoou/app
    case $1 in
        db:migrate)
            CREATE_ONLY=false
            shift
            [[ $1 == "apply" ]] && db_apply && exit


            [[ $1 == "--create-only" ]] && shift && CREATE_ONLY=true
            activate_back
            cd ./app/back
            db_apply
            PYTHONPATH=$PYTHONPATH alembic revision --autogenerate $@
            [[ $CREATE_ONLY == false ]] && db_apply
            ;;
        
        db:reset)
            DB_NAME=herokoou_db
            TERMINATE_CONECTIONS="SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '$DB_NAME' AND pid <> pg_backend_pid();"
            
            echo -e "\nReset database\n"
            psql "postgresql://admin:admin@localhost/postgres" -q \
                -c "$TERMINATE_CONECTIONS" \
                -c "drop database $DB_NAME" \
                -c "create database $DB_NAME"

            
            echo -e "\nDatabase reseted \n"
            ;;

        *) 
            echo "Command not found"
            ;;
    esac
    
}


[[ $1 == "dev" ]] && shift && dev_commands $@
