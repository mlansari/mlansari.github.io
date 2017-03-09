drop table if exists blog;
create table blog (
    id integer not null primary key autoincrement,
    title text not null,
    subtitle text not null,
    'text' text not null
);