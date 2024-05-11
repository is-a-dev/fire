CREATE TABLE config (
  guild_id BIGINT PRIMARY KEY UNIQUE,
  help_forum_id BIGINT NOT NULL,
  ping_role_id BIGINT NOT NULL
);

CREATE TABLE threads (
  thread_id BIGINT PRIMARY KEY,
  help_forum_id BIGINT NOT NULL,
  guild_id BIGINT NOT NULL,
  author_id BIGINT NOT NULL,
  has_first_message BOOLEAN NOT NULL DEFAULT FALSE,
  closed BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (guild_id) REFERENCES config(guild_id)
);

CREATE TABLE helpban (
  user_id BIGINT PRIMARY KEY,
  banner_id BIGINT NOT NULL,
  guild_id BIGINT NOT NULL,
  reason TEXT,
  FOREIGN KEY (guild_id) REFERENCES config(guild_id)
);
