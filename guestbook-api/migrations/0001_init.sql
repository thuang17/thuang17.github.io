-- One table: top-level messages (parent_id NULL) and replies (parent_id = the message)
CREATE TABLE posts (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  parent_id  INTEGER REFERENCES posts(id) ON DELETE CASCADE,
  author     TEXT NOT NULL CHECK (author IN ('visitor', 'owner')),
  nickname   TEXT NOT NULL,
  body       TEXT NOT NULL,
  status     TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
  token_hash TEXT,            -- hash of the visitor's browser token (never the token itself)
  ip_hash    TEXT,            -- salted hash, used only for rate limiting
  created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX idx_posts_parent ON posts(parent_id);
CREATE INDEX idx_posts_status ON posts(status, id);
CREATE INDEX idx_posts_ip ON posts(ip_hash, created_at);
