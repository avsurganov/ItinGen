class CreatePevents < ActiveRecord::Migration[5.2]
  def change
    create_table :pevents do |t|
      t.string :venue_id
      t.string :event_name
      t.string :event_alias
      t.string :event_id
      t.integer :mon_start
      t.integer :mon_end
      t.integer :tues_start
      t.integer :tues_end
      t.integer :wed_start
      t.integer :wed_end
      t.integer :thurs_start
      t.integer :thurs_end
      t.integer :fri_start
      t.integer :fri_end
      t.integer :sat_start
      t.integer :sat_end
      t.integer :sun_start
      t.integer :sun_end
      t.string :tags, array: true
      t.integer :price
    end
  end
end
