class CreateTevents < ActiveRecord::Migration[5.2]
  def change
    create_table :tevents do |t|
      t.string :venue_id
      t.string :event_name
      t.string :event_id
      t.integer :start
      t.integer :end
      t.string :date
      t.string :tags, array: true
      t.integer :price
    end
  end
end
