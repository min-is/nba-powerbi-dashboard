CREATE OR REPLACE FUNCTION validate_player_stats()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.three_point_attempted < NEW.three_point_made THEN
        RAISE EXCEPTION 'Invalid 3PT stats: Made % exceeds Attempted %',
            NEW.three_point_made, NEW.three_point_attempted;
    END IF;
    
    IF NEW.minutes_played > 48 THEN
        RAISE EXCEPTION 'Invalid minutes played: % exceeds regulation game time',
            NEW.minutes_played;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;