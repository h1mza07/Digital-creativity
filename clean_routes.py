# clean_routes.py
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Supprimer toutes les tables routes
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'routes_%'")
tables = [t[0] for t in c.fetchall()]

print("Tables routes trouvées:", tables)

for table in tables:
    c.execute(f'DROP TABLE IF EXISTS {table}')
    print(f"✅ Table {table} supprimée")

# Supprimer les métadonnées de migration
c.execute("DELETE FROM django_migrations WHERE app='routes'")
print("✅ Métadonnées routes supprimées")

conn.commit()
conn.close()

print("\n✅ Nettoyage complet terminé !")