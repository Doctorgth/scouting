


class database():
    ip="database"
    username="sample_user"
    db_name="db_name"
    password="sample_pass"
    port="5432"
    url=f"postgresql://{username}:{password}@{ip}:{port}/{db_name}"
